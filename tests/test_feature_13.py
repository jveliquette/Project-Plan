from django.contrib.auth.models import User
from django.test import TestCase, Client
from django.urls import reverse
from django.utils import timezone

from .utils import Document


class FeatureTests(TestCase):
    def setUp(self):
        try:
            from projects.models import Project  # noqa: F401
        except ModuleNotFoundError:
            self.fail("Could not find 'projects.models.Project'")
        self.client = Client()
        self.noor_credentials = {"username": "noor", "password": "1234abcd."}
        self.noor = User.objects.create_user(**self.noor_credentials)
        self.alisha = User.objects.create_user(
            username="alisha", password="1234abcd."
        )
        self.client.post(reverse("login"), self.noor_credentials)
        self.project = Project.objects.create(
            name="ZZZZZZ", description="AAAAA"
        )
        self.project.owner = self.noor
        self.project.save()

    def test_project_detail_returns_200(self):
        path = reverse("show_project", args=[self.project.id])
        response = self.client.get(path)
        self.assertEqual(
            response.status_code,
            200,
            msg="Did not get a 200 for project details",
        )

    def test_project_detail_shows_title(self):
        path = reverse("show_project", args=[self.project.id])
        response = self.client.get(path)
        document = Document()
        document.feed(response.content.decode("utf-8"))
        html = document.select("html")
        self.assertIn(
            "ZZZZZZ",
            html.inner_text(),
            msg="Did not find the project name on the page",
        )

    def test_project_detail_with_no_tasks_shows_message(self):
        path = reverse("show_project", args=[self.project.id])
        response = self.client.get(path)
        document = Document()
        document.feed(response.content.decode("utf-8"))
        html = document.select("html")
        self.assertIn(
            "This project has no tasks",
            html.inner_text(),
            msg="Did not find the 'no tasks' message on the page",
        )

    def test_project_detail_with_a_tasks_shows_task_name(self):
        try:
            from tasks.models import Task  # noqa: F401
        except ModuleNotFoundError:
            self.fail("Could not find 'tasks.models.Task'")
        task = Task.objects.create(
            name="YYYYYY",
            start_date=timezone.now(),
            due_date=timezone.now(),
            project=self.project,
            assignee=self.noor,
        )
        path = reverse("show_project", args=[self.project.id])
        response = self.client.get(path)
        document = Document()
        document.feed(response.content.decode("utf-8"))
        html = document.select("html")
        self.assertIn(
            task.name,
            html.inner_text(),
            msg="Did not find the task name in the detail page",
        )

    def test_project_detail_with_a_tasks_shows_task_start_date(self):
        try:
            from tasks.models import Task  # noqa: F401
        except ModuleNotFoundError:
            self.fail("Could not find 'tasks.models.Task'")
        task = Task.objects.create(
            name="YYYYYY",
            start_date=timezone.now(),
            due_date=timezone.now(),
            project=self.project,
            assignee=self.noor,
        )
        path = reverse("show_project", args=[self.project.id])
        response = self.client.get(path)
        document = Document()
        document.feed(response.content.decode("utf-8"))
        html = document.select("html")
        self.assertIn(
            str(task.start_date.year),
            html.inner_text(),
            msg="Did not find the task start date in the detail page",
        )

    def test_project_detail_with_a_tasks_shows_task_due_date(self):
        try:
            from tasks.models import Task  # noqa: F401
        except ModuleNotFoundError:
            self.fail("Could not find 'tasks.models.Task'")
        task = Task.objects.create(
            name="YYYYYY",
            start_date=timezone.now(),
            due_date=timezone.now(),
            project=self.project,
            assignee=self.noor,
        )
        path = reverse("show_project", args=[self.project.id])
        response = self.client.get(path)
        document = Document()
        document.feed(response.content.decode("utf-8"))
        html = document.select("html")
        self.assertIn(
            str(task.due_date.year),
            html.inner_text(),
            msg="Did not find the task due date in the detail page",
        )

    def test_project_detail_with_a_tasks_shows_assignee(self):
        try:
            from tasks.models import Task  # noqa: F401
        except ModuleNotFoundError:
            self.fail("Could not find 'tasks.models.Task'")
        Task.objects.create(
            name="YYYYYY",
            start_date=timezone.now(),
            due_date=timezone.now(),
            project=self.project,
            assignee=self.noor,
        )
        path = reverse("show_project", args=[self.project.id])
        response = self.client.get(path)
        document = Document()
        document.feed(response.content.decode("utf-8"))
        html = document.select("html")
        self.assertIn(
            self.noor.username,
            html.inner_text(),
            msg="Did not find the task assignee in the detail page",
        )

    def test_project_detail_with_a_tasks_shows_is_completed(self):
        try:
            from tasks.models import Task  # noqa: F401
        except ModuleNotFoundError:
            self.fail("Could not find 'tasks.models.Task'")
        Task.objects.create(
            name="YYYYYY",
            start_date=timezone.now(),
            due_date=timezone.now(),
            project=self.project,
            assignee=self.noor,
        )
        path = reverse("show_project", args=[self.project.id])
        response = self.client.get(path)
        document = Document()
        document.feed(response.content.decode("utf-8"))
        html = document.select("html")
        self.assertIn(
            "no",
            html.inner_text(),
            msg="Did not find the task is completed in the detail page",
        )

    def test_project_detail_with_a_tasks_shows_name_header(self):
        try:
            from tasks.models import Task  # noqa: F401
        except ModuleNotFoundError:
            self.fail("Could not find 'tasks.models.Task'")
        Task.objects.create(
            name="YYYYYY",
            start_date=timezone.now(),
            due_date=timezone.now(),
            project=self.project,
            assignee=self.noor,
        )
        path = reverse("show_project", args=[self.project.id])
        response = self.client.get(path)
        document = Document()
        document.feed(response.content.decode("utf-8"))
        html = document.select("html")
        self.assertIn(
            "Name",
            html.inner_text(),
            msg="Did not find the header 'Name' in the detail page",
        )

    def test_project_detail_with_a_tasks_shows_assignee_header(self):
        try:
            from tasks.models import Task  # noqa: F401
        except ModuleNotFoundError:
            self.fail("Could not find 'tasks.models.Task'")
        Task.objects.create(
            name="YYYYYY",
            start_date=timezone.now(),
            due_date=timezone.now(),
            project=self.project,
            assignee=self.noor,
        )
        path = reverse("show_project", args=[self.project.id])
        response = self.client.get(path)
        document = Document()
        document.feed(response.content.decode("utf-8"))
        html = document.select("html")
        self.assertIn(
            "Assignee",
            html.inner_text(),
            msg="Did not find the header 'Assignee' in the detail page",
        )

    def test_project_detail_with_a_tasks_shows_start_date_header(self):
        try:
            from tasks.models import Task  # noqa: F401
        except ModuleNotFoundError:
            self.fail("Could not find 'tasks.models.Task'")
        Task.objects.create(
            name="YYYYYY",
            start_date=timezone.now(),
            due_date=timezone.now(),
            project=self.project,
            assignee=self.noor,
        )
        path = reverse("show_project", args=[self.project.id])
        response = self.client.get(path)
        document = Document()
        document.feed(response.content.decode("utf-8"))
        html = document.select("html")
        self.assertIn(
            "Start date",
            html.inner_text(),
            msg="Did not find the header 'Start date' in the detail page",
        )

    def test_project_detail_with_a_tasks_shows_due_date_header(self):
        try:
            from tasks.models import Task  # noqa: F401
        except ModuleNotFoundError:
            self.fail("Could not find 'tasks.models.Task'")
        Task.objects.create(
            name="YYYYYY",
            start_date=timezone.now(),
            due_date=timezone.now(),
            project=self.project,
            assignee=self.noor,
        )
        path = reverse("show_project", args=[self.project.id])
        response = self.client.get(path)
        document = Document()
        document.feed(response.content.decode("utf-8"))
        html = document.select("html")
        self.assertIn(
            "Due date",
            html.inner_text(),
            msg="Did not find the header 'Due date' in the detail page",
        )

    def test_project_detail_with_a_tasks_shows_is_completed_header(self):
        try:
            from tasks.models import Task  # noqa: F401
        except ModuleNotFoundError:
            self.fail("Could not find 'tasks.models.Task'")
        Task.objects.create(
            name="YYYYYY",
            start_date=timezone.now(),
            due_date=timezone.now(),
            project=self.project,
            assignee=self.noor,
        )
        path = reverse("show_project", args=[self.project.id])
        response = self.client.get(path)
        document = Document()
        document.feed(response.content.decode("utf-8"))
        html = document.select("html")
        self.assertIn(
            "Is completed",
            html.inner_text(),
            msg="Did not find the header 'Is completed' in the detail page",
        )

    def test_project_list_has_link_to_project(self):
        path = reverse("list_projects")
        project_path = reverse("show_project", args=[self.project.id])
        response = self.client.get(path)
        document = Document()
        document.feed(response.content.decode("utf-8"))
        html = document.select("html")
        children = html.get_all_children("a")
        detail_link = None
        for child in children:
            if child.attrs.get("href") == project_path:
                detail_link = child
                break
        self.assertIsNotNone(
            detail_link,
            msg="Did not find the detail link for the project in the page",
        )

    def test_project_list_has_number_of_tasks(self):
        try:
            from tasks.models import Task  # noqa: F401
        except ModuleNotFoundError:
            self.fail("Could not find 'tasks.models.Task'")
        Task.objects.create(
            name="YYYYYY",
            start_date=timezone.now(),
            due_date=timezone.now(),
            project=self.project,
            assignee=self.noor,
        )
        path = reverse("list_projects")
        response = self.client.get(path)
        document = Document()
        document.feed(response.content.decode("utf-8"))
        html = document.select("html")
        self.assertIn(
            "1",
            html.inner_text(),
            msg="Did not find the number of tasks for the project in the page",
        )
