# Sciencemag
Coding challenge for Data Engineer role at Gemography.

### Purpose
Create a solution that crawls for articles from a news website, cleanses the response, stores in a mongo database then makes it available to search via an API.

### Solution
Scrapy based bot that crawls sciencemag.org website for lastest science news articles and stores them in a MongoDB server.

(Challenge only partly done due to my limited coding skills. Hopefully I'll have the oppotunity to nurture my skills at Gemography.)

### TODO
- Create one spider to fetch and store URLs and another one to use the URLs to access articles and crawl the data.
- Clean up the articles text and other details.
- Store the data in a hosted Mongo database instead of a local one.
- Write an API that grants access to the mongo database.

