from flask import Flask

pets = {
    'dogs': [
        {
            'name': 'Spot',
            'age': 2,
            'breed': 'Dalmatian',
            'description': 'Spot is an energetic puppy who seeks fun and adventure!',
            'url': 'https://content.codecademy.com/programs/flask/introduction-to-flask/dog-spot.jpeg'
        },
        {
            'name': 'Shadow',
            'age': 4,
            'breed': 'Border Collie',
            'description': 'Eager and curious, Shadow enjoys company and can always be found tagging along at your heels!',
            'url': 'https://content.codecademy.com/programs/flask/introduction-to-flask/dog-shadow.jpeg'
        }
    ],
    'cats': [
        {
            'name': 'Snowflake',
            'age': 1,
            'breed': 'Tabby',
            'description': 'Snowflake is a playful kitten who loves roaming the house and exploring.',
            'url': 'https://content.codecademy.com/programs/flask/introduction-to-flask/cat-snowflake.jpeg'
        }
    ],
    'rabbits': [
        {
            'name': 'Easter',
            'age': 4,
            'breed': 'Mini Rex',
            'description': 'Easter is a sweet, gentle rabbit who likes spending most of the day sleeping.',
            'url': 'https://content.codecademy.com/programs/flask/introduction-to-flask/rabbit-easter.jpeg'
        }
    ]
}

app = Flask(__name__)


@app.route('/')
def welcome():
    return'''
    <html>
        <body>
            <h1>Adopt a Pet!</h1>
            <p> Browse through the links below to find your new furry friend </p>
            <ul>
                <li><a href= '/dogs'>Dogs</a><br></li>
                <li><a href= '/cats'>Cats</a><br></li>
                <li><a href= '/rabbits'>Rabbits</a><br></li>
            </ul>
        </body>
    </html>
    '''

@app.route('/<pet_type>')
def animals(pet_type):
    
    html=f"<h1>List of {pet_type}</h1>"
    html+="<ul>" 

    for idx, item in enumerate(pets[pet_type]):
        html+=f'<li><a href= "/{pet_type}/{idx}">{item["name"]}</a></li>'

    html+="</ul>"

    return html

@app.route( '/<pet_type>/<int:pet_Id>')
def pet(pet_type, pet_Id):
    pet = pets[pet_type][pet_Id]
    return f'''
    <html>
        <body>
            <h2>Welcome Animals Page</h2><br>
            <img src="{pet['url']}" />
            <h2>{pet['name']}</h2>
            <p>{pet['age']}</p>
            <p>{pet['breed']}</p>
            <p>{pet['description']}</p>          
        </body>
    </html>
    '''

app.run(debug=True)






