
"""Track applicants and generate a simple recruitment report."""

import csv
import sqlite3

CONN = sqlite3.connect(":memory:")
CONN.execute(
    """
    CREATE TABLE applicants (
        id INTEGER PRIMARY KEY,
        name TEXT,
        role TEXT,
        expected_salary INTEGER,
        status TEXT
    )
    """
)


def add_applicant(name, role, expected_salary, status="applied"):
    """Add an applicant to the database."""
    CONN.execute(
        """
        INSERT INTO applicants
        (name, role, expected_salary, status)
        VALUES (?, ?, ?, ?)
        """,
        (name, role, expected_salary, status),
    )
    CONN.commit()


def shortlist(role, salary_limit):
    """Return applicants whose expected salary fits the limit."""
    rows = CONN.execute(
        """
        SELECT name, expected_salary
        FROM applicants
        WHERE role = ?
        """,
        (role,),
    ).fetchall()

    return [
        name
        for name, salary in rows
        if salary <= salary_limit
    ]


def update_status(applicant_id, status):
    """Update an applicant's hiring status."""
    try:
        CONN.execute(
            "UPDATE applicants SET status = ? WHERE id = ?",
            (status, applicant_id),
        )
        CONN.commit()
    except sqlite3.Error as error:
        print(f"Could not update applicant status: {error}")


def export_report(path):
    """Export applicant names, roles, and statuses to a CSV file."""
    with open(path, "w", encoding="utf-8", newline="") as report_file:
        writer = csv.writer(report_file)
        writer.writerow(["name", "role", "status"])
        rows = CONN.execute(
            "SELECT name, role, status FROM applicants"
        )
        writer.writerows(rows)


def count_by_status(status):
    """Return the number of applicants with a given status."""
    row = CONN.execute(
        "SELECT COUNT(*) FROM applicants WHERE status = ?",
        (status,),
    ).fetchone()
    return row[0]


def main():
    """Run a demonstration of the recruitment tracker."""
    add_applicant("Nina", "analyst", 600000)
    add_applicant("Omar", "analyst", 750000, "interview")
    add_applicant("Priya", "developer", 900000)

    update_status(1, "interview")

    print(shortlist("analyst", 650000))
    export_report("applicants_report.csv")
    print(count_by_status("interview"), "in interview")


if __name__ == "__main__":
    main()
