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
