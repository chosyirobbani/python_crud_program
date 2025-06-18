## Python CRUD Application for Student Data Management

A Python console application designed to manage stodent records using Create, Read, Update, and Delete (CRUD) operations.

## Business Understanding

This project supports educational institutions in effiiently managing student records. From student enrollment to data updates and deletions, the application ensures streamlined data processing, reducing manual work and minimizing errors.

**Benefits:**

* Improved Data Accuracy: Centralized system to minimize duplication or inconsistency in student information.
* Faster Decision-Making: Quick access to student performance data (e.g., exam scores) for teachers or administrators.
* Enhanced Record Management: Organized student data improves reporting and tracking over time.
* Data Retention Control: Recycle bin feature helps prevent accidental data loss and allows recovery.

**Target Users:**

This application is intended for school administrators, teachers, and academic support staff who need to manage and access student information quickly and accurately.

## Features

* **Create:**
    * Add new student records by providing:
      * NIS (unique 5-digit student ID)
      * Name
      * Gender (selection-based input)
      * Origin City
      * Exam Score (0–100)
   * Built-in validation to ensure input correctness and uniqueness of NIS.
* **Read:**
    * View all student records in a tabular format.
    * perform:
      * sorting: By student name (A-Z or Z-A).
      * searching: By NIS, name, gender, city of origin, or exam score.
    * Well-structured display with headers for easy reading.
* **Update:**
    * Modify student details based on NIS.
    * Select and update specific fields:
      * Name
      * Gender
      * City of Origin
      * Exam Score
    * Confirmation prompts ensure data is intentionally updated.
* **Delete:**
    * Remove a student from the active list using NIS.
    * Soft Delete system:
      * Deleted records are moved to a recycle bin instead of being permanently deleted.
      * Enables recovery if needed.
* **Recycle Bin:**
    * Stores deleted records.
    * Viewable for auditing or recovery purposes.
    * Enhances data safety and accountability.
## Installation

1. **Prerequisites:**
    * Python 3.7 or newer (no external packages needed)

2. **Installation:**
    ```bash
    git clone [https://github.com/](https://github.com/)<your-username>/python-inventory-crud.git
    cd python-inventory-crud
    pip install -r requirements.txt
    ```
3. **Database Setup:**
    * Create a PostgreSQL database and configure the connection details in `config.py`.

## Usage

1. **Run the application:**
    ```bash
    python main.py
    ```

2. **CRUD Operations:**
    * **Create:** Add a new student by entering details such as NIS (student ID), name, gender, city of origin, and exam score.
    * **Read:** View all student records in a tabular format. Sort or search based on name, NIS, gender, origin, or score.
    * **Update:** Modify a student's existing data (e.g., change their name, score, or origin city) using NIS as the reference.
    * **Delete:**  Remove a student from the list by NIS. The data is soft-deleted and stored in a recycle bin.
    * **Reports:** View deleted student records for reference or recovery.

## Data Model

This application uses in-memory data storage through Python lists and dictionaries (no database required). The data is structured as follows:

* **Student Records (data_siswa):**
   * NIS (Integer, Primary Key): Unique 5-digit student ID.
   * nama (String): Student's name
   * jenis kelamin (Sring): Gender (laki-laki / perempuan).
   * asal (String): City of origin.
   * nilai (Integer): Exam score (0–100).

* **Student Records (data_siswa):**
Same structure as data_siswa, used to store removed records for audit or restoration purposes.    
