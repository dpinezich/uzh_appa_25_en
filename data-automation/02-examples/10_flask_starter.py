import flask

# Create the application.
APP = flask.Flask(__name__)

@APP.route('/')
def index():
    """ Displays the index page accessible at '/' found in templates
    """
    return flask.render_template('10_hrdata_modified.html')


if __name__ == '__main__':
    APP.debug=True
    APP.run(host='0.0.0.0', port=5001)