# Recipe WebApp

Welcome to the Recipe WebApp! This app allows users to create, save, and search for recipes using ingredients. We utilize the MealDB API to fetch a wide variety of recipes.

## Features

- **Create Recipes**: Users can create their own recipes by inputting ingredients, instructions, and other details.
- **Save Recipes**: Save your favorite recipes for easy access later.
- **Search by Ingredients**: Use the MealDB API to search for recipes based on the ingredients you have on hand.
- **CRUD API**: The app includes a CRUD (Create, Read, Update, Delete) API for managing recipes in the backend.
- **Identity Server**: WSO2 Identity Server is integrated into the application to facilitate secure user login and authentication as well as user management.”
## CRUD API

The app provides a CRUD API for managing recipes. Here are the endpoints:

- **Create Recipe**: `POST /api/create-recipes`
- **Read Recipes**: `GET /api/list-recipes/`
- **Update Recipe**: `PUT /api/<str:name>/update`
- **Delete Recipe**: `DELETE /api/<str:name>/delete`

## Technologies Used

- **Bootstrap**: For design and user interface.
- **JavaScript**: For client-side logic.
- **CSS**: For application styling.
- **HTML**: For page structure.
- **Django**: As the server-side framework.
- **Python**: For backend logic.

## Contributing

We welcome contributions! Please fork the repository and submit pull requests.

## License

This project is licensed under the GPL License.

## Acknowledgements

- [TheMealDB](https://www.themealdb.com) for providing the API
- All the contributors and users for their support
