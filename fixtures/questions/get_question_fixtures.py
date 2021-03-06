true = True
false = False
null = None

get_question_query = '''{
  feedbackQuestion {
    totalResponses
    responses {
      roomName,
      responseCount,
      cleanlinessRating
    }
  }
}
'''

get_question_query_response = {
  "data": {
    "feedbackQuestion": {
      "totalResponses": 2,
      "responses": [
        {
          "roomName": "Entebbe",
          "responseCount": 2,
          "cleanlinessRating": 2
        }
      ]
    }
  }
}

get_paginated_question = '''{
  feedbackQuestion(page:1, perPage:1) {
    hasNext,
    hasPrevious,
    pages
    totalResponses
    responses {
      roomName,
      responseCount,
      cleanlinessRating
    }
  }
}
'''

get_paginated_question_query_response = {
  "data": {
    "feedbackQuestion": {
      "hasNext": false,
      "hasPrevious": false,
      "pages": 1,
      "totalResponses": 2,
      "responses": [
        {
          "roomName": "Entebbe",
          "responseCount": 2,
          "cleanlinessRating": 2
        }
      ]
    }
  }
}

get_paginated_question_invalid_page = '''{
  feedbackQuestion(page:100, perPage:5) {
    hasNext,
    hasPrevious,
    pages
    totalResponses
    responses {
      roomName,
      responseCount,
      cleanlinessRating
    }
  }
}
'''

all_questions_query = '''
query {
  questions{
    questions{
      id
      questionType
      question
      startDate
      endDate
      questionResponseCount
      response {
        id
        questionId
        roomId
      }
    }
  }
}
'''

all_questions_query_response = {
    'data': {
        'questions': {
            'questions': [{
                'id':
                '1',
                'questionType':
                'rate',
                'question':
                'How will you rate the brightness of the room',
                'startDate':
                '20 Nov 2018',
                'endDate':
                '28 Nov 2018',
                'questionResponseCount':
                1,
                'response': [{
                    'id': '1',
                    'questionId': 1,
                    'roomId': 1
                }]
            },
                          {
                              'id': '2',
                              'questionType': 'check',
                              'question':
                              'Is there anything missing in the room',
                              'startDate': '20 Nov 2018',
                              'endDate': '28 Nov 2018',
                              'questionResponseCount': 1,
                              'response': [{
                                  'id': '2',
                                  'questionId': 2,
                                  'roomId': 1
                              }]
                          },
                          {
                              'id': '3',
                              'questionType': 'input',
                              'question': 'Any other suggestion',
                              'startDate': '20 Nov 2018',
                              'endDate': '28 Nov 2018',
                              'questionResponseCount': 0,
                              'response': []
                          }]
        }
    }
}

paginated_all_questions_query = '''
query {
  questions(page:1, perPage:2){
    questions{
      id
      questionType
      question
      startDate
      endDate
      questionResponseCount
      response {
        id
        questionId
        roomId
      }
    }
  }
}
'''

paginated_all_questions_query_response = {
    'data': {
        'questions': {
            'questions': [{
                'id':
                '1',
                'questionType':
                'rate',
                'question':
                'How will you rate the brightness of the room',
                'startDate':
                '20 Nov 2018',
                'endDate':
                '28 Nov 2018',
                'questionResponseCount':
                1,
                'response': [{
                    'id': '1',
                    'questionId': 1,
                    'roomId': 1
                }]
            },
                          {
                              'id': '2',
                              'questionType': 'check',
                              'question':
                              'Is there anything missing in the room',
                              'startDate': '20 Nov 2018',
                              'endDate': '28 Nov 2018',
                              'questionResponseCount': 1,
                              'response': [{
                                  'id': '2',
                                  'questionId': 2,
                                  'roomId': 1
                              }]
                          }]
        }
    }
}

get_question_by_id_query = '''
query {
  question(id:1){
    id
    questionType
    question
    startDate
    endDate
    questionResponseCount
    response {
      id
      questionId
      roomId
    }
  }
}
'''

get_question_by_id_query_response = {
    'data': {
        'question': {
            'id': '1',
            'questionType': 'rate',
            'question': 'How will you rate the brightness of the room',
            'startDate': '20 Nov 2018',
            'endDate': '28 Nov 2018',
            'questionResponseCount': 1,
            'response': [{
                'id': '1',
                'questionId': 1,
                'roomId': 1
            }]
        }
    }
}

get_question_invalid_id_query = '''
query {
  question(id:122){
    id
    questionType
    question
    startDate
    endDate
    questionResponseCount
    response {
      id
      questionId
      roomId
    }
  }
}
'''
