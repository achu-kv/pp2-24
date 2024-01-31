# task 1
def is_higher_55(movie):
    return movie["imdb"] > 5.5

# task 2
def good_films(movies):
    out = []
    for i in movies:
        if is_higher_55(i):
            out.append(i)
    return out

# task 3
def under_category(movies, category):
    out = []
    for i in movies:
        if i["category"] == category:
            out.append(i)
    return out

# task 4
def average_imdb(movies):
    if len(movies) == 0:
        return 0
    total = 0
    for i in movies:
        total += i["imdb"]
    return total / len(movies)

# task 5
def avg_of_category(movies, category):
    return average_imdb(under_category(movies, category))


movies = [
{
"name": "Usual Suspects", 
"imdb": 7.0,
"category": "Thriller"
},
{
"name": "Hitman",
"imdb": 6.3,
"category": "Action"
},
{
"name": "Dark Knight",
"imdb": 9.0,
"category": "Adventure"
},
{
"name": "The Help",
"imdb": 8.0,
"category": "Drama"
},
{
"name": "The Choice",
"imdb": 6.2,
"category": "Romance"
},
{
"name": "Colonia",
"imdb": 7.4,
"category": "Romance"
},
{
"name": "Love",
"imdb": 6.0,
"category": "Romance"
},
{
"name": "Bride Wars",
"imdb": 5.4,
"category": "Romance"
},
{
"name": "AlphaJet",
"imdb": 3.2,
"category": "War"
},
{
"name": "Ringing Crime",
"imdb": 4.0,
"category": "Crime"
},
{
"name": "Joking muck",
"imdb": 7.2,
"category": "Comedy"
},
{
"name": "What is the name",
"imdb": 9.2,
"category": "Suspense"
},
{
"name": "Detective",
"imdb": 7.0,
"category": "Suspense"
},
{
"name": "Exam",
"imdb": 4.2,
"category": "Thriller"
},
{
"name": "We Two",
"imdb": 7.2,
"category": "Romance"
}
]


