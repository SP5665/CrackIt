CREATE TABLE users (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(150) NOT NULL UNIQUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE resumes (
    id INT PRIMARY KEY AUTO_INCREMENT,
    user_id INT NOT NULL,
    file_name VARCHAR(255) NOT NULL,
    file_type VARCHAR(50) NOT NULL,
    parsed_data JSON,
    uploaded_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY (user_id) REFERENCES users(id)
);

CREATE TABLE interview_sessions (
    id INT PRIMARY KEY AUTO_INCREMENT,
    user_id INT NOT NULL,
    resume_id INT,
    role VARCHAR(100) NOT NULL,
    status ENUM('IN_PROGRESS', 'COMPLETED') DEFAULT 'IN_PROGRESS',
    started_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    completed_at TIMESTAMP NULL,

    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (resume_id) REFERENCES resumes(id)
);

CREATE TABLE questions (
    id INT PRIMARY KEY AUTO_INCREMENT,
    interview_session_id INT NOT NULL,
    parent_question_id INT NULL,
    question_text TEXT NOT NULL,
    question_type VARCHAR(50),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY (interview_session_id) REFERENCES interview_sessions(id),
    FOREIGN KEY (parent_question_id) REFERENCES questions(id)
);

CREATE TABLE answers (
    id INT PRIMARY KEY AUTO_INCREMENT,
    question_id INT NOT NULL,
    interview_session_id INT NOT NULL,
    answer_text TEXT NOT NULL,

    relevance_score DECIMAL(4,2),
    specificity_score DECIMAL(4,2),
    technical_depth_score DECIMAL(4,2),
    clarity_score DECIMAL(4,2),

    decision VARCHAR(30),
    evaluator_feedback TEXT,

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY (question_id) REFERENCES questions(id),
    FOREIGN KEY (interview_session_id) REFERENCES interview_sessions(id)
);