# WordCount

## Technology Stack 

1. Flask
2. Mongo

## Assumption

Word as a string that contains a number or letter

```
"Apple" is a word
"Cat" is a word
"@#$" is NOT a word
"I am " is NOT a word, t is sentence
"123" is a word
"Abc_123" is a word
```

## Steps to run the application 

1. Go to the root application folder(i.e WordCount) and run the below command

```docker-compose up -d```

2. Open Postman/terminal to run the APIs

GET API

```curl --location --request GET 'http://0.0.0.0:5000/word/cds' \
--header 'Content-Type: application/json'```

PUT API

```curl --location --request PUT 'http://0.0.0.0:5000/word/apple' \
--header 'Content-Type: application/json'```

