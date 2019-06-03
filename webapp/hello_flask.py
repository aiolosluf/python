from flask import Flask, render_template, request, escape
from vsearch import search4letters

app = Flask(__name__)


@app.route('/search4', methods=['POST'])
def do_search() -> 'html':
    phrase = request.form['phrase']
    letters = request.form['letters']
    title = 'Here are your results:'
    results = str(search4letters(phrase, letters))
    log_request(request,results)
    return render_template('results.html',the_title=title,
                           the_phrase=phrase,the_letters=letters,the_results=results,)


@app.route('/')
@app.route('/entry')
def entry_page() -> 'html':
    return render_template('entry.html',the_title='Welcome to search4letters on the web!')


@app.route('/viewlog')
def view_log() -> 'html':
    contents = []
    with open('vsearch.log') as log:
    #     contents = log.readlines()
    # return escape(''.join(contents))
        for eachLine in log:
            contents.append(eachLine.split('|'))
    # return str(contents)
    return render_template('viewlog.html',the_title='Log',the_row_titles=['Form Data','Remote_addr','User_agent','Results'],
                           the_data=contents)


def log_request(req: 'flask_request',res: str) -> None:
    with open('vsearch.log','a') as task:
        # print(str(dir(req)),res,file=task)
        # print(req.form, file=task, end='|')
        # print(req.remote_addr, file=task, end='|')
        # print(req.user_agent, file=task, end='|')
        # print(res, file=task)
        print(req.form, req.remote_addr, req.user_agent, res, file=task, sep='|')


if __name__ == '__main__':
    app.run(debug=True)