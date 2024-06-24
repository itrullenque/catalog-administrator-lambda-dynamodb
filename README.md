# Catalog API Documentation

This document outlines the usage of the Catalog API endpoints.

## Base URL

https://[your-api-gateway-id].execute-api.[your-region].amazonaws.com/dev

## Endpoints

### 1. Create a Catalog Item (POST /catalog)

Creates a new catalog item.

Query Parameters:

- catalog_id (required): Unique identifier for the catalog
- course_id (required): Identifier for the course

Example: POST /catalog?catalog_id=cat123&course_id=course456

Response:

- 200 OK: Item created successfully
- 400 Bad Request: Missing or incorrect parameters
- 500 Internal Server Error: Server-side error

### 2. Get a Catalog Item (GET /catalog)

Retrieves a specific catalog item.

Query Parameters:

- catalog_id (required): Unique identifier for the catalog
- course_id (required): Identifier for the course

Example: GET /catalog?catalog_id=cat123&course_id=course456

Response:

- 200 OK: Returns the catalog item
- 400 Bad Request: Missing or incorrect parameters
- 500 Internal Server Error: Server-side error

### 3. Delete a Catalog Item (DELETE /catalog)

Deletes a specific catalog item.

Query Parameters:

- catalog_id (required): Unique identifier for the catalog
- course_id (required): Identifier for the course

Example: DELETE /catalog?catalog_id=cat123&course_id=course456

Response:

- 200 OK: Item deleted successfully
- 400 Bad Request: Missing or incorrect parameters
- 500 Internal Server Error: Server-side error

### 4. Query Catalog Items (GET /catalogquery)

Queries catalog items based on academic year or course ID.

Query Parameters (use one, not both):

- academic_year: Filter by academic year
- course_id: Filter by course ID

Examples:

- GET /catalogquery?academic_year=2023
- GET /catalogquery?course_id=course456

Response:

- 200 OK: Returns matching catalog items
- 400 Bad Request: Invalid or missing query parameters
- 500 Internal Server Error: Server-side error

### 5. Get All Catalog Items (GET /catalogs)

Retrieves all catalog items.

No query parameters accepted.

Example: GET /catalogs

Response:

- 200 OK: Returns all catalog items
- 400 Bad Request: If any query parameters are provided
- 500 Internal Server Error: Server-side error

## Notes

- All responses are in JSON format.
- The POST request automatically sets the academic year to the current year.
- The API uses DynamoDB with Global Secondary Indexes for academic_year and course_id.
- CORS is enabled for all endpoints.
