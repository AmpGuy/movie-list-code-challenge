from bottle import Bottle, run, route, error, request
import unittest
import sys, os

app = Bottle()

movie_titles = {
	'Resident Evil' : {
		'released':'2002',
		'production': 'Screen Gems/Constantin Films/Davis Films'
	},
	'Resident Evil: Apocalypse' : {
		'released':'2004',
		'production': 'Screen Gems/Constantin Films/Davis Films'
	},
	'Resident Evil: Extinction' : {
		'released':'2007',
		'production': 'Screen Gems/Constantin Films/Davis Films'
	}
}

@app.error(404)
def error404(error):
	return 'No API method found!'

@app.route('/api/movies/', method='GET')
@app.route('/api/movies/<name>', method='GET')
def getMovie(name = ''):
    	if name == '':
        	return('Here are ALL the movies: %s\n' % movie_titles)
    	elif name in movie_titles:
        	movie = movie_titles[name]
        	return('Movie named %s was released in %s and the production company is %s\n' % (name, movie['released'], movie['production']))
    	else:
        	return('No movie with this name %s !\n' % name)

@app.route('/api/movies/<name>', method='POST')
def addMovie(name=''):

	if name in movie_titles:
		return('The title %s is already in the database.\n' % name)
	else:
		released = request.forms.get( "released" )
		production = request.forms.get( "production" )
		movie_titles[name] = {
       			'released': released,
			'production': production
		}

	return ('Created a new movie title: %s\n' % name)

@app.route('/api/movies/<name>', method='PUT')
def updateMovie(name=""):
	released = request.forms.get( "released" )
	production = request.forms.get( "production" )
    	if name in movie_titles:
		flic = movie_titles[name]
       		flic['released'] = released or flic['released']
		flic['production'] = production or flic['production']

       		return('Movie %s, the release date is now %s and the production company is %s\n' % (name, flic['released'], flic['production']))
	else:
       		return('No movie with the title %s found!\n' % name)

@app.route('/api/movies/<name>', method='DELETE')
def deleteMovie(name=""):
	if name in movie_titles:
      		movie_titles.pop(name)
		return('Movie with the title %s has been deleted.\n' % name)
    	else:
		return('No movie with the title %s found!\n' % name)

if __name__ == '__main__':
	run(app, reloader=True, host='localhost', port=8080)
