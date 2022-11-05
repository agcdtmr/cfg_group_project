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


def display_saved_jobs(employerId: int, employerName: str, expirationDate: str, jobDescription: str, jobId: int, jobTitle: str,
jobURL: str, locationName: str, maximumSalary: int, minimumSalary: int, user_ID: int, have_i_applied: str):

    with get_database_connection() as connection:
        with connection.cursor(dictionary=True) as cursor:
            cursor.execute("""INSERT
                               SELECT sj.employerID AS 'Employer ID', sj.employerName AS 'Employer Name',
                                sj.expirationDate AS 'Date Application Closes', sj.jobID AS 'Job ID',
                                 sj.jobTitle AS 'Job Title', sj.jobURL AS 'Link to Apply',
                                  sj.locationName AS 'Location', sj.maximumSalary AS 'Maximum Salary',
                                   sj.minimumSalary AS 'Minimum Salary',
                                    sj.applied_for_job AS 'Have I applied for this job?'
                                    FROM saved_jobs AS sj """,
                           [employerId, employerName, expirationDate, jobDescription, jobId, jobTitle, jobURL,
                            locationName, maximumSalary, minimumSalary, user_ID, have_i_applied])
            connection.commit()
