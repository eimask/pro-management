from datetime import datetime
from app import db
from app.module_base.models import Base


class Task(Base):
    __tablename__ = 'TASK'

    task_code = db.Column(db.String(128), nullable=False, unique=True)
    task_name = db.Column(db.String(225))
    task_type = db.Column(db.String(3))
    man_days_quoted = db.Column(db.Float, default=0)
    man_days_dev = db.Column(db.Float, default=0)
    main_sa = db.Column(db.String(128))
    status = db.Column(db.String(3))
    assigned_by = db.Column(db.String(128))
    assigned_date = db.Column(db.DateTime, default=datetime.utcnow())
    dev_code = db.Column(db.String(128))
    est_start_date_dev = db.Column(db.DateTime)
    est_end_date_dev = db.Column(db.DateTime)
    qa_code = db.Column(db.String(128))
    est_start_date_qa = db.Column(db.DateTime)
    est_end_date_qa = db.Column(db.DateTime)
    description = db.Column(db.String(2000))
    parent_task_id = db.Column(db.Integer)
    project_id = db.Column(db.Integer, nullable=True)
    priority = db.Column(db.Integer)

    def __init__(self, task_code, task_name, task_type, man_days_quoted, man_days_dev, main_sa, status, assigned_by,
                 assigned_date, dev_code, est_start_date_dev, est_end_date_dev, qa_code, est_start_date_qa,
                 est_end_date_qa, description, parent_task_id, project_id, priority):
        self.task_code = task_code
        self.task_name = task_name
        self.task_type = task_type
        self.man_days_quoted = man_days_quoted
        self.man_days_dev = man_days_dev
        self.main_sa = main_sa
        self.status = status
        self.assigned_by = assigned_by
        self.assigned_date = assigned_date
        self.dev_code = dev_code
        self.est_start_date_dev = est_start_date_dev
        self.est_end_date_dev = est_end_date_dev
        self.qa_code = qa_code
        self.est_start_date_qa = est_start_date_qa
        self.est_end_date_qa = est_end_date_qa
        self.description = description
        self.parent_task_id = parent_task_id
        self.project_id = project_id
        self.priority = priority

    def __repr__(self):
        return '<Task {}>'.format(self.task_code)
