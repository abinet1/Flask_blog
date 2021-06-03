from Flask_blog import app


@app.route('/')
def index():
	return "Blog Project Stated."

