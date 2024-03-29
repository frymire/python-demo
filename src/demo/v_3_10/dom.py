import xml.dom.minidom

# Open XML document using minidom parser
DOMTree = xml.dom.minidom.parse("../../../resources/movies.xml")
collection = DOMTree.documentElement
if collection.hasAttribute("shelf"):
    print(f'\nRoot element: {collection.getAttribute("shelf")}')

# Get all the movies in the collection
movies = collection.getElementsByTagName("movie")

# Print detail of each movie.
for movie in movies:

    print("\n*****Movie*****")
    if movie.hasAttribute("title"):
        print("Title: %s" % movie.getAttribute("title"))

    print("Type: %s" % movie.getElementsByTagName('type')[0].childNodes[0].data)
    print("Format: %s" % movie.getElementsByTagName('format')[0].childNodes[0].data)
    print("Rating: %s" % movie.getElementsByTagName('rating')[0].childNodes[0].data)
    print("Description: %s" % movie.getElementsByTagName('description')[0].childNodes[0].data)
