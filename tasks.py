from flask import Blueprint, redirect, render_template, request, url_for
from flask_login import current_user, login_required

from models import Task, db

tasks_bp = Blueprint("tasks", __name__)


def find_task(task_id):
    return Task.query.filter_by(id=task_id, user_id=current_user.id).first()


@tasks_bp.route("/")
@login_required
def index():
    user_id = current_user.id
    pending = Task.query.filter_by(user_id=user_id, completed=False).order_by(
        Task.created_at.desc()
    ).all()
    completed = Task.query.filter_by(user_id=user_id, completed=True).order_by(
        Task.created_at.desc()
    ).all()
    return render_template("tasks.html", pending_tasks=pending, completed_tasks=completed)


@tasks_bp.route("/tasks/add", methods=["POST"])
@login_required
def add_task():
    title = (request.form.get("title") or "").strip()
    description = (request.form.get("description") or "").strip()
    if not title:
        return redirect(url_for("tasks.index"))

    t = Task(title=title, description=description, user_id=current_user.id)
    db.session.add(t)
    db.session.commit()
    return redirect(url_for("tasks.index"))


@tasks_bp.route("/tasks/<int:task_id>/edit", methods=["GET", "POST"])
@login_required
def edit_task(task_id):
    t = find_task(task_id)
    if not t:
        return redirect(url_for("tasks.index"))

    if request.method == "POST":
        title = (request.form.get("title") or "").strip()
        description = (request.form.get("description") or "").strip()
        if not title:
            return render_template("edit_task.html", task=t)

        t.title = title
        t.description = description
        db.session.commit()
        return redirect(url_for("tasks.index"))

    return render_template("edit_task.html", task=t)


@tasks_bp.route("/tasks/<int:task_id>/delete", methods=["POST"])
@login_required
def delete_task(task_id):
    t = find_task(task_id)
    if not t:
        return redirect(url_for("tasks.index"))
    db.session.delete(t)
    db.session.commit()
    return redirect(url_for("tasks.index"))


@tasks_bp.route("/tasks/<int:task_id>/toggle", methods=["POST"])
@login_required
def toggle_task(task_id):
    t = find_task(task_id)
    if not t:
        return redirect(url_for("tasks.index"))
    t.completed = not t.completed
    db.session.commit()
    return redirect(url_for("tasks.index"))
