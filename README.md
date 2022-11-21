# Game reviews database

## Description

This is a database of PlayStation 5 games with their respective metascores from two review aggregator sites. A metascore is a value given by the site based on all the reviews made for a game. There are two review aggregator sites, Metacritic and Opencritic.

The final idea of this database is to be able to calculate a final metascore value taking into account the metascores of each page separately.

In this first version of the database and REST API, we are only working on accessing the basic values and functions of the database, i.e. an index of each entity, displaying value by id, and creating and deleting data.

## API Reference Table

### Games

**GET /games**
Returns a list of games in the database with their respective information.

**GET /games/:id**
Returns the information about a single game specified by the requested ID.
*Path parameters*
- **id: string**. The ID of a registered game in the database.

**POST /games**
Create a new game in the database.
*JSON body paramethers*
- **name**: *type* **string**: Name of the game
- **genre**: *type* **string**: Genre of the game
- **esrb_rating**: *type* **string**: ESRB rating of the game
- **release_date**: *type* **date**: Release date of the game
- **multiplayer**: *type* **boolean**: True if the game allows multiplayer mode. False if not.
- **developer_id**: *type* **integer**: The id of the developer's game, registered in the database.
- **publisher_id**: *type* **integer**: The id of the publisher's game, registered in the database.

**DELETE /games/:id**
Delete a game specified by the requested ID. 
*Path parameters*
- **id: string**. The ID of a registered game in the database.
*Response fields*
- *type* **boolean**: Indicates whether the game was deleted as a result of this request.

### Publishers

**GET /publishers**
Returns a list of publishers in the database.

**GET /publishers/:id**
Returns the information about a single publisher specified by the requested ID.
*Path parameters*
- **id: string**. The ID of a registered publisher in the database.

**POST /publishers**
Create a new publisher in the database.
*JSON body paramethers*
- **name**: *type* **string**: Name of the publisher

**DELETE /publisher/:id**
Delete a publisher specified by the requested ID. 
*Path parameters*
- **id: string**. The ID of a registered publisher in the database.
*Response fields*
- *type* **boolean**: Indicates whether the publisher was deleted as a result of this request.

### Developers

**GET /developers**
Returns a list of developers in the database.

**GET /developers/:id**
Returns the information about a single developer specified by the requested ID.
*Path parameters*
- **id: string**. The ID of a registered developer in the database.

**POST /developers**
Create a new developer in the database.
*JSON body paramethers*
- **name**: *type* **string**: Name of the developer

**DELETE /developers/:id**
Delete a developer specified by the requested ID. 
*Path parameters*
- **id: string**. The ID of a registered developer in the database.
*Response fields*
- *type* **boolean**: Indicates whether the developer was deleted as a result of this request.

### Platforms

**GET /platforms**
Returns a list of platforms in the database.

**GET /platform/:id**
Returns the information about a single platform specified by the requested ID.
*Path parameters*
- **id: string**. The ID of a registered platform in the database.

### Review sites

**GET /review_sites**
Returns a list of review sites aggregator in the database.

**GET /platform/:id**
Returns the information about a single review site specified by the requested ID.
*Path parameters*
- **id: string**. The ID of a registered review site in the database.

# Questions

**How did the project's design evolve over time?**
The project has not evolved from the initial idea, but this version does not meet that objective. The basic functions of the database have been implemented with the idea that in later versions the goal of establishing the final metascore for each game can be met.

**Did you choose to use an ORM or raw SQL? Why?**
I chose to use an ORM because for me it is more interesting to explore the versatility that Python has to perform different tasks. I am not yet completely comfortable with SQL.

**What future improvements are in store, if any?**
Many improvements are foreseen for the future, as this version does not reach its target. First of all is to be able to make a request to calculate the final metascore for a given game, filter metascores by platform, developer, etc. And for a more distant future, maybe to be able to feed my database automatically.