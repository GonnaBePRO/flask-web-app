import requests
import pymysql

pymysql.install_as_MySQLdb()
import MySQLdb

connection = MySQLdb.connect("localhost", "majkel", "localhost", "majkel_flask")


def testHttpStatus():
    test_url = "http://localhost:5000/"

    response = requests.get(test_url)
    assert response.status_code == 200


def testRowAmount():
    # SQL RETURN ROW COUNT
    cursor = connection.cursor()
    cursor.execute("SELECT COUNT(*) FROM comments")
    row = cursor.fetchone()
    assert row[0] > 0


def testPostComment():
    test_url = "http://localhost:5000/contact"

    data = {"email": "test@mail.com", "message": "joł benc"}

    assert requests.post(test_url, data)


def testDeleting():
    cursor = connection.cursor()
    assert cursor.execute("DELETE FROM comments ORDER BY id DESC LIMIT 1;")
