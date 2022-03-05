def score_server():
    # import flask package
    import webbrowser
    from flask import Flask, render_template
    from Utils import SCORES_FILE_NAME

    # create a flask application. we will use it to run the app later
    app = Flask(__name__)

    # define an http path to match a python function, in this case when going to http://127.0.0.1:5000/
    # this function will be called. it's return will be used to response the http call
    @app.route('/')
    def home():

        try:
            with open(SCORES_FILE_NAME, 'r') as sc:
                points = sc.readline()
                print(points)
                return render_template("score.html", SCORE=points)
        except FileNotFoundError:
            return render_template("error.html", ERROR="error! failed to find score")
            # main scope for python

    if __name__ == '__main__':
        # Open browser :
        #webbrowser.open("http://127.0.0.1:5000")
        # run the flask application itself. here we can configure it's listen port and address
        app.run(host="0.0.0.0",port=5000,debug=True)


score_server()
