

def test_delete_first_contact(app):
    app.open_home_page()
    app.session.login("admin", "secret")
    app.contact.delete_first_contact()
    app.session.logout()
