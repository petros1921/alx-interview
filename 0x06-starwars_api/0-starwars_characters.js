#!/usr/bin/node

async function getMovieCharacters(movieId) {
  const baseUrl = 'https://swapi.dev/api/films/';

  try {
      // Fetch the film data
      const response = await fetch(${baseUrl}${movieId}/);
      if (!response.ok) {
          throw new Error('Network response was not ok');
      }
      const filmData = await response.json();

      // Extract the characters list
      const charactersUrls = filmData.characters;

      // Fetch and print each character's name
      for (const url of charactersUrls) {
          try {
              const charResponse = await fetch(url);
              if (!charResponse.ok) {
                  throw new Error('Network response was not ok');
              }
              const characterData = await charResponse.json();
              console.log(characterData.name);
          } catch (error) {
              console.error('An error occurred while fetching character data:', error);
          }
      }
  } catch (error) {
      console.error('An error occurred:', error);
  }
}

// Get the movie ID from the command line arguments
const movieId = process.argv[2];

if (!movieId) {
  console.error('Usage: node script.js <Movie ID>');
  process.exit(1);
}

getMovieCharacters(movieId);