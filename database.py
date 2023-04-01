from sqlalchemy import create_engine, text

db_connection_string = "mysql+pymysql://8yy589ed1juvmrnyblk8:pscale_pw_IcJ0fNE1vICxsk0qzkrIiJr2up7QBWIHW7RFlAg2fWG@aws.connect.psdb.cloud/pythoncareers?charset=utf8mb4"

engine = create_engine(db_connection_string,
                       connect_args={"ssl": {
                         "ssl_ca": "/etc/ssl/cert.pem"
                       }})


def load_jobs_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("select * from jobs"))
    column_names = result.keys()

    jobs = []

    for row in result.all():
      jobs.append(dict(zip(column_names, row)))

    return jobs


def load_job_from_db(id):
  with engine.connect() as conn:
    result = conn.execute(text(f"SELECT * FROM jobs WHERE id={id}"))
    rows = []
    column_name = result.keys()
    for row in result.all():
      rows.append(dict(zip(column_name, row)))
    if len(rows) == 0:
      return None
    else:
      return (rows[0])


def add_application_to_db(job_id, data):
  with engine.connect() as conn:
    query = text(
      "INSERT INTO applications (job_id, full_name, email, linkedin_url, education, work_experience, resume_url) VALUES (:job_id, :full_name, :email, :linkedin_url, :education, :work_experience, :resume_url)"
    )

    conn.execute(query,
                 job_id=job_id,
                 full_name=data['full_name'],
                 email=data['email'],
                 linkedin_url=data['linkedin_url'],
                 education=data['education'],
                 work_experience=data['work_experience'],
                 resume_url=data['resume_url'])


print(load_job_from_db(1))