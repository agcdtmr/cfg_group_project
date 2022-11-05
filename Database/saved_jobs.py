from Database.connection import get_database_connection

def save_job(employerId: int, employerName: str, expirationDate: str, jobDescription: str, jobId: int, jobTitle: str,
jobURL: str, locationName: str, maximumSalary: int, minimumSalary: int, user_ID: int):
    """
    Adds a job user wants to apply for to database
    """
    with get_database_connection() as connection:
        with connection.cursor(dictionary=True) as cursor:
            cursor.execute("""INSERT
                               INTO saved_jobs
                                  (employerID, employerName,expirationDate, jobDescription, jobID, jobTitle,
                                   jobURL, locationName, maximumSalary, minimumSalary, user_ID)
                                   VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""",
                           [employerId, employerName, expirationDate, jobDescription, jobId, jobTitle, jobURL,
                            locationName, maximumSalary, minimumSalary, user_ID])
            connection.commit()


def display_saved_jobs():
    with get_database_connection() as connection:
        with connection.cursor(dictionary=True) as cursor:
            cursor.execute("""SELECT sj.jobID,
                                sj.employerName AS 'Employer Name',
                                sj.expirationDate AS 'Date Application Closes',
                                 sj.jobTitle AS 'Job Title', sj.jobURL AS 'Link to Apply',
                                  sj.locationName AS 'Location', sj.maximumSalary AS 'Maximum Salary',
                                   sj.minimumSalary AS 'Minimum Salary',
                                    sj.applied_for_job AS 'Have I applied for this job?'
                                    FROM saved_jobs AS sj""",)
            retrieved_data = cursor.fetchall()
            if retrieved_data is not None:
                return retrieved_data


def save_applied_for_job(jobID):
    """
    Adds have i applied for job when clicking link to apply for job
    """
    with get_database_connection() as connection:
        with connection.cursor(dictionary=True) as cursor:
            cursor.execute("""UPDATE saved_jobs
            SET applied_for_job = TRUE
            WHERE jobID = %s """,
                           [jobID])
            connection.commit()