'''Flask is nothing but a small/micro web framework used to create small web apps.
From converting the console based application into a web app we need to understand a new
concept which is known as Flask.

'''

from flask import Flask, render_template, request  # importing the flask library to run our web app.

app = Flask(__name__)  # we are initializing Flask

@app.route("/") #we are directing our web page to perform a function.

#Define visitor function
def visitors():

    # Load current count
    counter_read_file = open("count.txt", "r")
    visitors_count = int(counter_read_file.read())
    counter_read_file.close()

    # Increment the count
    visitors_count = visitors_count + 1

    # Overwrite the count
    counter_write_file = open("count.txt", "w")
    counter_write_file.write(str(visitors_count))
    counter_write_file.close()

    # Render HTML with count variable : means This method displays the HTML page along with count on the web.
    return render_template("index.html", count=visitors_count)

@app.route('/', methods=['POST'])  # POST will help us to fetch data from the input field.

def covid_stats():
    # Load current count
    counter_read_file = open("count.txt", "r")
    visitors_count = int(counter_read_file.read())
    counter_read_file.close()

    text = request.form['text']  #We are requesting text from the HTML page as input

    corona_data = 'https://covidstats-sdbd.onrender.com/?country='+text
    print(corona_data)
    #below- return corona_data as image and visitors count data at HTML page
    return render_template("index.html", image=corona_data, count=visitors_count)


# it will run our web app on localhost.
if __name__ == "__main__":
    app.run()
