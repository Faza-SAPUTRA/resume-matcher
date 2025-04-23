from flask import Flask, request, render_template
import os
import docx2txt
import PyPDF2
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'Uploads')

def extract_text_from_pdf(file_path):
    text = ""
    try:
        with open(file_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            for page in reader.pages:
                text += page.extract_text() or ""
    except Exception as e:
        print(f"Error extracting PDF from {file_path}: {e}")
    return text

def extract_text_from_docx(file_path):
    try:
        return docx2txt.process(file_path)
    except Exception as e:
        print(f"Error extracting DOCX from {file_path}: {e}")
        return ""

def extract_text_from_txt(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except Exception as e:
        print(f"Error extracting TXT from {file_path}: {e}")
        return ""

def extract_text(file_path):
    try:
        if not os.path.exists(file_path):
            print(f"Error: File not found: {file_path}")
            return ""
        if file_path.endswith('.pdf'):
            return extract_text_from_pdf(file_path)
        elif file_path.endswith('.docx') or file_path.endswith('.doc'):
            return extract_text_from_docx(file_path)
        elif file_path.endswith('.txt'):
            return extract_text_from_txt(file_path)
        else:
            print(f"Error: Unsupported file type: {file_path}")
            return ""
    except Exception as e:
        print(f"Error extracting text from {file_path}: {e}")
        return ""

def humanize_similarity_score(score):
    percentage = round(score * 100)
    if score >= 0.75:
        label = "Cocok Sekali"
    elif score >= 0.50:
        label = "Sangat Cocok"
    elif score >= 0.30:
        label = "Cukup Cocok"
    elif score >= 0.20:
        label = "Cocok Sedang"
    elif score >= 0.10:
        label = "Kurang Cocok"
    else:
        label = "Tidak Cocok"
    return percentage, label

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/matcher", methods=['GET', 'POST'])
def matcher():
    if request.method == 'POST':
        job_description = request.form.get('jobDescription')
        resume_files = request.files.getlist('fileInput')

        if not resume_files or not job_description:
            return render_template('matcher.html', message="Mohon unggah resume dan masukkan deskripsi pekerjaan.")

        resumes = []
        valid_resume_files = []
        for resume_file in resume_files:
            if resume_file.filename == '':
                continue
            filename = secure_filename(resume_file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            try:
                resume_file.save(filepath)
                text = extract_text(filepath)
                if text:
                    resumes.append(text)
                    valid_resume_files.append(resume_file)
                else:
                    print(f"Warning: No text extracted from {filename}")
            except Exception as e:
                print(f"Error saving or processing {filename}: {e}")
                continue

        if not resumes:
            return render_template('matcher.html', message="Tidak ada resume yang valid untuk diproses. Periksa format file.")

        try:
            vectorizer = TfidfVectorizer().fit_transform([job_description] + resumes)
            vectors = vectorizer.toarray()

            job_vector = vectors[0]
            resume_vectors = vectors[1:]
            similarities = cosine_similarity([job_vector], resume_vectors)[0]

            top_indices = similarities.argsort()[-5:][::-1]
            top_resumes = [valid_resume_files[i].filename for i in top_indices]
            similarity_scores = [humanize_similarity_score(similarities[i]) for i in top_indices]

            return render_template('matcher.html', 
                                 message="Resume dengan kecocokan tertinggi:", 
                                 top_resumes=top_resumes, 
                                 similarity_scores=similarity_scores)
        except Exception as e:
            print(f"Error in vectorization or similarity calculation: {e}")
            return render_template('matcher.html', message="Terjadi kesalahan saat memproses resume. Silakan coba lagi.")

    return render_template('matcher.html')

@app.errorhandler(FileNotFoundError)
def handle_file_not_found(e):
    return render_template('matcher.html', message=f"Kesalahan akses file: {str(e)}. Periksa jalur file dan izin."), 500

@app.errorhandler(Exception)
def handle_generic_error(e):
    print(f"Unexpected error: {e}")
    return render_template('matcher.html', message="Terjadi kesalahan tak terduga. Silakan coba lagi."), 500

if __name__ == '__main__':
    try:
        if not os.path.exists(app.config['UPLOAD_FOLDER']):
            os.makedirs(app.config['UPLOAD_FOLDER'])
            print(f"Created directory: {app.config['UPLOAD_FOLDER']}")
        else:
            print(f"Directory already exists: {app.config['UPLOAD_FOLDER']}")
        test_file = os.path.join(app.config['UPLOAD_FOLDER'], 'test.txt')
        with open(test_file, 'w') as f:
            f.write('test')
        os.remove(test_file)
        print("Write permission verified for UPLOAD_FOLDER")
    except PermissionError:
        print(f"Error: No permission to create or write to {app.config['UPLOAD_FOLDER']}")
        raise
    except Exception as e:
        print(f"Error setting up UPLOAD_FOLDER: {e}")
        raise
    app.run(debug=True)