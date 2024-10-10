<!-- #region(collapsed) [NAME] -->
{{collapse(Версия (тест))
<pre>
    front
    5cfa84a6 dev 482911
    #131975  test-circuit  40ce2f3d 
    Evgeniy Serobaba
</pre>
}}
<!-- #endregion --> 
%{color:green}Содержимое%
<!-- #region(collapsed) [NAME] -->
{{collapse(Работа эндпоинтов:)
<pre><code class='shell'>
TRUE

Request URL:
https://lk-test.egais.ru/api-lc-license/dashboard/license/request/page?filter=%5B%5B%22status.finishedStatus%22,%22=%22,%22false%22%5D,%22and%22,%5B%22deliveryCode%22,%22=%22,5%5D%5D&sort=-dateInsert&page=0&size=20
Request Method:
GET
Status Code:
200 OK

filter: [["status.finishedStatus","=","false"],"and",["deliveryCode","=",5]]
sort: -dateInsert
page: 0
size: 20

FALSE

Request URL:
https://lk-test.egais.ru/api-lc-license/dashboard/license/request/page?filter=%5B%5B%22status.finishedStatus%22,%22=%22,%22false%22%5D,%22and%22,%5B%22deliveryCode%22,%22%3C%3E%22,5%5D%5D&sort=-dateInsert&page=0&size=20
Request Method:
GET
Status Code:
200 OK

filter: [["status.finishedStatus","=","false"],"and",["deliveryCode","<>",5]]
sort: -dateInsert
page: 0
size: 20
</code></pre>
}}
<!-- #endregion --> 


<!-- #region(collapsed) [NAME] -->
{{collapse(Положительный фильтр код = 5)
<pre><code class='json'>
{
    "content": [
        {
            "requestId": 225415,
            "inn": "576853595470",
            "organization": "ИП Попова Д. А.",
            "orgBriefName": null,
            "orgFullName": null,
            "deloNum": "Л-874",
            "dateInsert": "2024-10-09T10:46:01.297",
            "dateChange": "2024-10-09T10:50:57.674045",
            "regNum": null,
            "deloDate": "2024-10-09",
            "regDate": null,
            "licenseType": {
                "code": 4,
                "description": "производство, хранение, поставки и розничная продажа произведенной сельскохозяйственными производителями винодельческой продукции",
                "shortName": "ПХПРП_СХП",
                "region": false
            },
            "attach": [
                {
                    "id": 12204,
                    "fileName": "576853595470_Л-874_1.pdf",
                    "ext": "pdf",
                    "type": {
                        "code": 0,
                        "name": "Не определено",
                        "signed": false
                    }
                },
                {
                    "id": 12205,
                    "fileName": "576853595470_Л-874_2.pdf",
                    "ext": "pdf",
                    "type": {
                        "code": 0,
                        "name": "Не определено",
                        "signed": false
                    }
                }
            ],
            "regionCode": "57",
            "status": {
                "code": 2001,
                "description": "На рассмотрении",
                "initialStatus": true,
                "finishedStatus": false
            },
            "indicator": {
                "finished": 9,
                "total": 26,
                "showPercent": true
            },
            "requestType": {
                "code": 7,
                "description": "Заявление о выдаче лицензии",
                "region": true
            },
            "reregTypes": null,
            "execUser": {
                "id": 121,
                "firstName": "Подрядчик",
                "middleName": null,
                "lastName": "АО 'ЦЕНТРИНФОРМ'"
            },
            "deliveryCode": 5,
            "finalResult": true,
            "rating": null,
            "newRegNum": null,
            "erulNumber": null,
            "suspensionSign": false,
            "indicationNum": null,
            "indicationColor": null,
            "statusCode": 2001,
            "description": "На рассмотрении",
            "requestTypeDescription": "Заявление о выдаче лицензии",
            "licenseTypeId": 4,
            "requestTypeId": 7
        },
        {
            "requestId": 225413,
            "inn": "576853595470",
            "organization": "ИП Попова Д. А.",
            "orgBriefName": null,
            "orgFullName": null,
            "deloNum": "Л-872",
            "dateInsert": "2024-10-08T16:57:19.117",
            "dateChange": "2024-10-09T10:36:57.745605",
            "regNum": null,
            "deloDate": "2024-10-08",
            "regDate": null,
            "licenseType": {
                "code": 4,
                "description": "производство, хранение, поставки и розничная продажа произведенной сельскохозяйственными производителями винодельческой продукции",
                "shortName": "ПХПРП_СХП",
                "region": false
            },
            "attach": [
                {
                    "id": 12202,
                    "fileName": "576853595470_Л-872_1.pdf",
                    "ext": "pdf",
                    "type": {
                        "code": 0,
                        "name": "Не определено",
                        "signed": false
                    }
                },
                {
                    "id": 12203,
                    "fileName": "576853595470_Л-872_2.pdf",
                    "ext": "pdf",
                    "type": {
                        "code": 0,
                        "name": "Не определено",
                        "signed": false
                    }
                }
            ],
            "regionCode": "57",
            "status": {
                "code": 2005,
                "description": "Приостановлено",
                "initialStatus": false,
                "finishedStatus": false,
                "requestResult": false
            },
            "indicator": {
                "finished": 11,
                "total": 26,
                "showPercent": true
            },
            "requestType": {
                "code": 7,
                "description": "Заявление о выдаче лицензии",
                "region": true
            },
            "reregTypes": null,
            "execUser": {
                "id": 103,
                "firstName": "Peter Petrovich",
                "middleName": null,
                "lastName": "Petrov"
            },
            "deliveryCode": 5,
            "finalResult": true,
            "rating": null,
            "newRegNum": null,
            "erulNumber": null,
            "suspensionSign": true,
            "indicationNum": 30,
            "indicationColor": "GREEN",
            "statusCode": 2005,
            "description": "Приостановлено",
            "requestTypeDescription": "Заявление о выдаче лицензии",
            "licenseTypeId": 4,
            "requestTypeId": 7
        },
        {
            "requestId": 225412,
            "inn": "576853595470",
            "organization": "ИП Попова Д. А.",
            "orgBriefName": null,
            "orgFullName": null,
            "deloNum": "Л-871",
            "dateInsert": "2024-10-08T16:54:22.663",
            "dateChange": "2024-10-08T16:58:06.581704",
            "regNum": null,
            "deloDate": "2024-10-08",
            "regDate": null,
            "licenseType": {
                "code": 4,
                "description": "производство, хранение, поставки и розничная продажа произведенной сельскохозяйственными производителями винодельческой продукции",
                "shortName": "ПХПРП_СХП",
                "region": false
            },
            "attach": [
                {
                    "id": 12200,
                    "fileName": "576853595470_Л-871_1.pdf",
                    "ext": "pdf",
                    "type": {
                        "code": 0,
                        "name": "Не определено",
                        "signed": false
                    }
                },
                {
                    "id": 12201,
                    "fileName": "576853595470_Л-871_2.pdf",
                    "ext": "pdf",
                    "type": {
                        "code": 0,
                        "name": "Не определено",
                        "signed": false
                    }
                }
            ],
            "regionCode": "57",
            "status": {
                "code": 2001,
                "description": "На рассмотрении",
                "initialStatus": true,
                "finishedStatus": false
            },
            "indicator": {
                "finished": 6,
                "total": 26,
                "showPercent": true
            },
            "requestType": {
                "code": 7,
                "description": "Заявление о выдаче лицензии",
                "region": true
            },
            "reregTypes": null,
            "execUser": {
                "id": 103,
                "firstName": "Peter Petrovich",
                "middleName": null,
                "lastName": "Petrov"
            },
            "deliveryCode": 5,
            "finalResult": true,
            "rating": null,
            "newRegNum": null,
            "erulNumber": null,
            "suspensionSign": false,
            "indicationNum": null,
            "indicationColor": null,
            "statusCode": 2001,
            "description": "На рассмотрении",
            "requestTypeDescription": "Заявление о выдаче лицензии",
            "licenseTypeId": 4,
            "requestTypeId": 7
        },
        {
            "requestId": 225411,
            "inn": "576853595470",
            "organization": "ИП Попова Д. А.",
            "orgBriefName": null,
            "orgFullName": null,
            "deloNum": "Л-870",
            "dateInsert": "2024-10-08T16:35:13.647",
            "dateChange": "2024-10-08T16:41:53.192611",
            "regNum": null,
            "deloDate": "2024-10-08",
            "regDate": null,
            "licenseType": {
                "code": 4,
                "description": "производство, хранение, поставки и розничная продажа произведенной сельскохозяйственными производителями винодельческой продукции",
                "shortName": "ПХПРП_СХП",
                "region": false
            },
            "attach": [
                {
                    "id": 12198,
                    "fileName": "576853595470_Л-870_1.pdf",
                    "ext": "pdf",
                    "type": {
                        "code": 0,
                        "name": "Не определено",
                        "signed": false
                    }
                },
                {
                    "id": 12199,
                    "fileName": "576853595470_Л-870_2.pdf",
                    "ext": "pdf",
                    "type": {
                        "code": 0,
                        "name": "Не определено",
                        "signed": false
                    }
                }
            ],
            "regionCode": "57",
            "status": {
                "code": 2001,
                "description": "На рассмотрении",
                "initialStatus": true,
                "finishedStatus": false
            },
            "indicator": {
                "finished": 9,
                "total": 26,
                "showPercent": true
            },
            "requestType": {
                "code": 7,
                "description": "Заявление о выдаче лицензии",
                "region": true
            },
            "reregTypes": null,
            "execUser": {
                "id": 103,
                "firstName": "Peter Petrovich",
                "middleName": null,
                "lastName": "Petrov"
            },
            "deliveryCode": 5,
            "finalResult": true,
            "rating": null,
            "newRegNum": null,
            "erulNumber": null,
            "suspensionSign": false,
            "indicationNum": null,
            "indicationColor": null,
            "statusCode": 2001,
            "description": "На рассмотрении",
            "requestTypeDescription": "Заявление о выдаче лицензии",
            "licenseTypeId": 4,
            "requestTypeId": 7
        },
        {
            "requestId": 225410,
            "inn": "7841051711",
            "organization": "АО «ЦентрИнформ» ",
            "orgBriefName": null,
            "orgFullName": null,
            "deloNum": "Л-868",
            "dateInsert": "2024-10-08T15:42:27.793",
            "dateChange": "2024-10-08T15:47:29.452724",
            "regNum": null,
            "deloDate": "2024-10-08",
            "regDate": null,
            "licenseType": {
                "code": 2,
                "description": "производство, хранение и поставки произведенной алкогольной продукции",
                "shortName": "ПХП_АП",
                "region": false
            },
            "attach": [
                {
                    "id": 12194,
                    "fileName": "7841051711_Л-868_7.pdf",
                    "ext": "pdf",
                    "type": {
                        "code": 0,
                        "name": "Не определено",
                        "signed": false
                    }
                },
                {
                    "id": 12195,
                    "fileName": "7841051711_Л-868_8.pdf",
                    "ext": "pdf",
                    "type": {
                        "code": 0,
                        "name": "Не определено",
                        "signed": false
                    }
                },
                {
                    "id": 12189,
                    "fileName": "7841051711_Л-868_2.pdf",
                    "ext": "pdf",
                    "type": {
                        "code": 0,
                        "name": "Не определено",
                        "signed": false
                    }
                },
                {
                    "id": 12190,
                    "fileName": "7841051711_Л-868_3.pdf",
                    "ext": "pdf",
                    "type": {
                        "code": 0,
                        "name": "Не определено",
                        "signed": false
                    }
                },
                {
                    "id": 12191,
                    "fileName": "7841051711_Л-868_4.pdf",
                    "ext": "pdf",
                    "type": {
                        "code": 0,
                        "name": "Не определено",
                        "signed": false
                    }
                },
                {
                    "id": 12193,
                    "fileName": "7841051711_Л-868_6.pdf",
                    "ext": "pdf",
                    "type": {
                        "code": 0,
                        "name": "Не определено",
                        "signed": false
                    }
                },
                {
                    "id": 12188,
                    "fileName": "7841051711_Л-868_1.pdf",
                    "ext": "pdf",
                    "type": {
                        "code": 0,
                        "name": "Не определено",
                        "signed": false
                    }
                },
                {
                    "id": 12192,
                    "fileName": "7841051711_Л-868_5.pdf",
                    "ext": "pdf",
                    "type": {
                        "code": 0,
                        "name": "Не определено",
                        "signed": false
                    }
                },
                {
                    "id": 12196,
                    "fileName": "7841051711_Л-868_9.pdf",
                    "ext": "pdf",
                    "type": {
                        "code": 0,
                        "name": "Не определено",
                        "signed": false
                    }
                },
                {
                    "id": 12197,
                    "fileName": "7841051711_Л-868_10.pdf",
                    "ext": "pdf",
                    "type": {
                        "code": 0,
                        "name": "Не определено",
                        "signed": false
                    }
                }
            ],
            "regionCode": "78",
            "status": {
                "code": 2001,
                "description": "На рассмотрении",
                "initialStatus": true,
                "finishedStatus": false
            },
            "indicator": {
                "finished": 12,
                "total": 22,
                "showPercent": true
            },
            "requestType": {
                "code": 7,
                "description": "Заявление о выдаче лицензии",
                "region": true
            },
            "reregTypes": null,
            "execUser": {
                "id": 121,
                "firstName": "Подрядчик",
                "middleName": null,
                "lastName": "АО 'ЦЕНТРИНФОРМ'"
            },
            "deliveryCode": 5,
            "finalResult": true,
            "rating": null,
            "newRegNum": null,
            "erulNumber": null,
            "suspensionSign": false,
            "indicationNum": null,
            "indicationColor": null,
            "statusCode": 2001,
            "description": "На рассмотрении",
            "requestTypeDescription": "Заявление о выдаче лицензии",
            "licenseTypeId": 2,
            "requestTypeId": 7
        },
        {
            "requestId": 225406,
            "inn": "7841051711",
            "organization": "АО «ЦентрИнформ» ",
            "orgBriefName": null,
            "orgFullName": null,
            "deloNum": "Л-864",
            "dateInsert": "2024-10-08T09:12:06.12",
            "dateChange": "2024-10-08T09:18:06.340786",
            "regNum": null,
            "deloDate": "2024-10-08",
            "regDate": null,
            "licenseType": {
                "code": 8,
                "description": "закупка, хранение и поставки алкогольной продукции",
                "shortName": "ЗХП_АП",
                "region": false
            },
            "attach": [
                {
                    "id": 12181,
                    "fileName": "7841051711_Л-864_2.pdf",
                    "ext": "pdf",
                    "type": {
                        "code": 0,
                        "name": "Не определено",
                        "signed": false
                    }
                },
                {
                    "id": 12182,
                    "fileName": "7841051711_Л-864_3.pdf",
                    "ext": "pdf",
                    "type": {
                        "code": 0,
                        "name": "Не определено",
                        "signed": false
                    }
                },
                {
                    "id": 12183,
                    "fileName": "7841051711_Л-864_4.pdf",
                    "ext": "pdf",
                    "type": {
                        "code": 0,
                        "name": "Не определено",
                        "signed": false
                    }
                },
                {
                    "id": 12184,
                    "fileName": "7841051711_Л-864_5.pdf",
                    "ext": "pdf",
                    "type": {
                        "code": 0,
                        "name": "Не определено",
                        "signed": false
                    }
                },
                {
                    "id": 12185,
                    "fileName": "7841051711_Л-864_6.pdf",
                    "ext": "pdf",
                    "type": {
                        "code": 0,
                        "name": "Не определено",
                        "signed": false
                    }
                },
                {
                    "id": 12180,
                    "fileName": "7841051711_Л-864_1.pdf",
                    "ext": "pdf",
                    "type": {
                        "code": 0,
                        "name": "Не определено",
                        "signed": false
                    }
                },
                {
                    "id": 12186,
                    "fileName": "7841051711_Л-864_7.pdf",
                    "ext": "pdf",
                    "type": {
                        "code": 0,
                        "name": "Не определено",
                        "signed": false
                    }
                },
                {
                    "id": 12187,
                    "fileName": "7841051711_Л-864_8.pdf",
                    "ext": "pdf",
                    "type": {
                        "code": 0,
                        "name": "Не определено",
                        "signed": false
                    }
                }
            ],
            "regionCode": "78",
            "status": {
                "code": 2001,
                "description": "На рассмотрении",
                "initialStatus": true,
                "finishedStatus": false
            },
            "indicator": {
                "finished": 11,
                "total": 21,
                "showPercent": true
            },
            "requestType": {
                "code": 7,
                "description": "Заявление о выдаче лицензии",
                "region": true
            },
            "reregTypes": null,
            "execUser": {
                "id": 103,
                "firstName": "Peter Petrovich",
                "middleName": null,
                "lastName": "Petrov"
            },
            "deliveryCode": 5,
            "finalResult": true,
            "rating": null,
            "newRegNum": null,
            "erulNumber": null,
            "suspensionSign": false,
            "indicationNum": null,
            "indicationColor": null,
            "statusCode": 2001,
            "description": "На рассмотрении",
            "requestTypeDescription": "Заявление о выдаче лицензии",
            "licenseTypeId": 8,
            "requestTypeId": 7
        },
        {
            "requestId": 225405,
            "inn": "7841051711",
            "organization": "АО «ЦентрИнформ» ",
            "orgBriefName": null,
            "orgFullName": null,
            "deloNum": "Л-863",
            "dateInsert": "2024-10-08T08:50:33.347",
            "dateChange": "2024-10-08T08:51:54.316357",
            "regNum": null,
            "deloDate": "2024-10-08",
            "regDate": null,
            "licenseType": {
                "code": 8,
                "description": "закупка, хранение и поставки алкогольной продукции",
                "shortName": "ЗХП_АП",
                "region": false
            },
            "attach": [
                {
                    "id": 12172,
                    "fileName": "7841051711_Л-863_1.pdf",
                    "ext": "pdf",
                    "type": {
                        "code": 0,
                        "name": "Не определено",
                        "signed": false
                    }
                },
                {
                    "id": 12173,
                    "fileName": "7841051711_Л-863_2.pdf",
                    "ext": "pdf",
                    "type": {
                        "code": 0,
                        "name": "Не определено",
                        "signed": false
                    }
                },
                {
                    "id": 12174,
                    "fileName": "7841051711_Л-863_3.pdf",
                    "ext": "pdf",
                    "type": {
                        "code": 0,
                        "name": "Не определено",
                        "signed": false
                    }
                },
                {
                    "id": 12175,
                    "fileName": "7841051711_Л-863_4.pdf",
                    "ext": "pdf",
                    "type": {
                        "code": 0,
                        "name": "Не определено",
                        "signed": false
                    }
                },
                {
                    "id": 12176,
                    "fileName": "7841051711_Л-863_5.pdf",
                    "ext": "pdf",
                    "type": {
                        "code": 0,
                        "name": "Не определено",
                        "signed": false
                    }
                },
                {
                    "id": 12177,
                    "fileName": "7841051711_Л-863_6.pdf",
                    "ext": "pdf",
                    "type": {
                        "code": 0,
                        "name": "Не определено",
                        "signed": false
                    }
                },
                {
                    "id": 12178,
                    "fileName": "7841051711_Л-863_7.pdf",
                    "ext": "pdf",
                    "type": {
                        "code": 0,
                        "name": "Не определено",
                        "signed": false
                    }
                },
                {
                    "id": 12179,
                    "fileName": "7841051711_Л-863_8.pdf",
                    "ext": "pdf",
                    "type": {
                        "code": 0,
                        "name": "Не определено",
                        "signed": false
                    }
                }
            ],
            "regionCode": "78",
            "status": {
                "code": 2001,
                "description": "На рассмотрении",
                "initialStatus": true,
                "finishedStatus": false
            },
            "indicator": {
                "finished": 10,
                "total": 21,
                "showPercent": true
            },
            "requestType": {
                "code": 7,
                "description": "Заявление о выдаче лицензии",
                "region": true
            },
            "reregTypes": null,
            "execUser": {
                "id": 103,
                "firstName": "Peter Petrovich",
                "middleName": null,
                "lastName": "Petrov"
            },
            "deliveryCode": 5,
            "finalResult": true,
            "rating": null,
            "newRegNum": null,
            "erulNumber": null,
            "suspensionSign": false,
            "indicationNum": null,
            "indicationColor": null,
            "statusCode": 2001,
            "description": "На рассмотрении",
            "requestTypeDescription": "Заявление о выдаче лицензии",
            "licenseTypeId": 8,
            "requestTypeId": 7
        },
        {
            "requestId": 225403,
            "inn": "7841051711",
            "organization": "АО «ЦентрИнформ» ",
            "orgBriefName": null,
            "orgFullName": null,
            "deloNum": "Л-859",
            "dateInsert": "2024-10-07T15:24:35.98",
            "dateChange": "2024-10-07T16:28:21.516843",
            "regNum": null,
            "deloDate": "2024-10-07",
            "regDate": null,
            "licenseType": {
                "code": 2,
                "description": "производство, хранение и поставки произведенной алкогольной продукции",
                "shortName": "ПХП_АП",
                "region": false
            },
            "attach": [
                {
                    "id": 12165,
                    "fileName": "7841051711_Л-859_2.pdf",
                    "ext": "pdf",
                    "type": {
                        "code": 0,
                        "name": "Не определено",
                        "signed": false
                    }
                },
                {
                    "id": 12166,
                    "fileName": "7841051711_Л-859_3.pdf",
                    "ext": "pdf",
                    "type": {
                        "code": 0,
                        "name": "Не определено",
                        "signed": false
                    }
                },
                {
                    "id": 12164,
                    "fileName": "7841051711_Л-859_1.pdf",
                    "ext": "pdf",
                    "type": {
                        "code": 0,
                        "name": "Не определено",
                        "signed": false
                    }
                },
                {
                    "id": 12168,
                    "fileName": "7841051711_Л-859_5.pdf",
                    "ext": "pdf",
                    "type": {
                        "code": 0,
                        "name": "Не определено",
                        "signed": false
                    }
                },
                {
                    "id": 12170,
                    "fileName": "7841051711_Л-859_7.pdf",
                    "ext": "pdf",
                    "type": {
                        "code": 0,
                        "name": "Не определено",
                        "signed": false
                    }
                },
                {
                    "id": 12171,
                    "fileName": "7841051711_Л-859_8.pdf",
                    "ext": "pdf",
                    "type": {
                        "code": 0,
                        "name": "Не определено",
                        "signed": false
                    }
                },
                {
                    "id": 12167,
                    "fileName": "7841051711_Л-859_4.pdf",
                    "ext": "pdf",
                    "type": {
                        "code": 0,
                        "name": "Не определено",
                        "signed": false
                    }
                },
                {
                    "id": 12169,
                    "fileName": "7841051711_Л-859_6.pdf",
                    "ext": "pdf",
                    "type": {
                        "code": 0,
                        "name": "Не определено",
                        "signed": false
                    }
                }
            ],
            "regionCode": "78",
            "status": {
                "code": 2006,
                "description": "Ожидает приостановления",
                "initialStatus": false,
                "finishedStatus": false,
                "requestResult": false
            },
            "indicator": {
                "finished": 12,
                "total": 22,
                "showPercent": true
            },
            "requestType": {
                "code": 7,
                "description": "Заявление о выдаче лицензии",
                "region": true
            },
            "reregTypes": null,
            "execUser": {
                "id": 103,
                "firstName": "Peter Petrovich",
                "middleName": null,
                "lastName": "Petrov"
            },
            "deliveryCode": 5,
            "finalResult": true,
            "rating": null,
            "newRegNum": null,
            "erulNumber": null,
            "suspensionSign": false,
            "indicationNum": null,
            "indicationColor": null,
            "statusCode": 2006,
            "description": "Ожидает приостановления",
            "requestTypeDescription": "Заявление о выдаче лицензии",
            "licenseTypeId": 2,
            "requestTypeId": 7
        },
        {
            "requestId": 225402,
            "inn": "7841051711",
            "organization": "АО «ЦентрИнформ» ",
            "orgBriefName": null,
            "orgFullName": null,
            "deloNum": "Л-858",
            "dateInsert": "2024-10-07T14:08:00.88",
            "dateChange": "2024-10-07T15:40:31.243461",
            "regNum": null,
            "deloDate": "2024-10-07",
            "regDate": null,
            "licenseType": {
                "code": 8,
                "description": "закупка, хранение и поставки алкогольной продукции",
                "shortName": "ЗХП_АП",
                "region": false
            },
            "attach": [
                {
                    "id": 12160,
                    "fileName": "7841051711_Л-858_5.pdf",
                    "ext": "pdf",
                    "type": {
                        "code": 0,
                        "name": "Не определено",
                        "signed": false
                    }
                },
                {
                    "id": 12156,
                    "fileName": "7841051711_Л-858_1.pdf",
                    "ext": "pdf",
                    "type": {
                        "code": 0,
                        "name": "Не определено",
                        "signed": false
                    }
                },
                {
                    "id": 12157,
                    "fileName": "7841051711_Л-858_2.pdf",
                    "ext": "pdf",
                    "type": {
                        "code": 0,
                        "name": "Не определено",
                        "signed": false
                    }
                },
                {
                    "id": 12158,
                    "fileName": "7841051711_Л-858_3.pdf",
                    "ext": "pdf",
                    "type": {
                        "code": 0,
                        "name": "Не определено",
                        "signed": false
                    }
                },
                {
                    "id": 12159,
                    "fileName": "7841051711_Л-858_4.pdf",
                    "ext": "pdf",
                    "type": {
                        "code": 0,
                        "name": "Не определено",
                        "signed": false
                    }
                },
                {
                    "id": 12161,
                    "fileName": "7841051711_Л-858_6.pdf",
                    "ext": "pdf",
                    "type": {
                        "code": 0,
                        "name": "Не определено",
                        "signed": false
                    }
                },
                {
                    "id": 12162,
                    "fileName": "7841051711_Л-858_7.pdf",
                    "ext": "pdf",
                    "type": {
                        "code": 0,
                        "name": "Не определено",
                        "signed": false
                    }
                },
                {
                    "id": 12163,
                    "fileName": "7841051711_Л-858_8.pdf",
                    "ext": "pdf",
                    "type": {
                        "code": 0,
                        "name": "Не определено",
                        "signed": false
                    }
                }
            ],
            "regionCode": "78",
            "status": {
                "code": 2005,
                "description": "Приостановлено",
                "initialStatus": false,
                "finishedStatus": false,
                "requestResult": false
            },
            "indicator": {
                "finished": 12,
                "total": 21,
                "showPercent": true
            },
            "requestType": {
                "code": 7,
                "description": "Заявление о выдаче лицензии",
                "region": true
            },
            "reregTypes": null,
            "execUser": {
                "id": 103,
                "firstName": "Peter Petrovich",
                "middleName": null,
                "lastName": "Petrov"
            },
            "deliveryCode": 5,
            "finalResult": true,
            "rating": null,
            "newRegNum": null,
            "erulNumber": null,
            "suspensionSign": true,
            "indicationNum": null,
            "indicationColor": null,
            "statusCode": 2005,
            "description": "Приостановлено",
            "requestTypeDescription": "Заявление о выдаче лицензии",
            "licenseTypeId": 8,
            "requestTypeId": 7
        },
        {
            "requestId": 225398,
            "inn": "7841051711",
            "organization": "АО «ЦентрИнформ» ",
            "orgBriefName": null,
            "orgFullName": null,
            "deloNum": "Л-851",
            "dateInsert": "2024-10-07T09:38:08.133",
            "dateChange": "2024-10-07T11:46:27.820949",
            "regNum": null,
            "deloDate": "2024-10-07",
            "regDate": null,
            "licenseType": {
                "code": 2,
                "description": "производство, хранение и поставки произведенной алкогольной продукции",
                "shortName": "ПХП_АП",
                "region": false
            },
            "attach": [
                {
                    "id": 12155,
                    "fileName": "7841051711_Л-851_1.pdf",
                    "ext": "pdf",
                    "type": {
                        "code": 0,
                        "name": "Не определено",
                        "signed": false
                    }
                }
            ],
            "regionCode": "78",
            "status": {
                "code": 2005,
                "description": "Приостановлено",
                "initialStatus": false,
                "finishedStatus": false,
                "requestResult": false
            },
            "indicator": {
                "finished": 13,
                "total": 22,
                "showPercent": true
            },
            "requestType": {
                "code": 7,
                "description": "Заявление о выдаче лицензии",
                "region": true
            },
            "reregTypes": null,
            "execUser": {
                "id": 121,
                "firstName": "Подрядчик",
                "middleName": null,
                "lastName": "АО 'ЦЕНТРИНФОРМ'"
            },
            "deliveryCode": 5,
            "finalResult": true,
            "rating": null,
            "newRegNum": null,
            "erulNumber": null,
            "suspensionSign": true,
            "indicationNum": null,
            "indicationColor": null,
            "statusCode": 2005,
            "description": "Приостановлено",
            "requestTypeDescription": "Заявление о выдаче лицензии",
            "licenseTypeId": 2,
            "requestTypeId": 7
        },
        {
            "requestId": 225395,
            "inn": "7841051711",
            "organization": "АО «ЦентрИнформ» ",
            "orgBriefName": null,
            "orgFullName": null,
            "deloNum": "Л-848",
            "dateInsert": "2024-10-04T19:00:24.403",
            "dateChange": "2024-10-04T19:05:00.645324",
            "regNum": null,
            "deloDate": "2024-10-04",
            "regDate": null,
            "licenseType": {
                "code": 3,
                "description": "производство, хранение и поставки произведенной сельскохозяйственными производителями винодельческой продукции",
                "shortName": "ПХП_СХП",
                "region": false
            },
            "attach": [
                {
                    "id": 12148,
                    "fileName": "7841051711_Л-848_1.pdf",
                    "ext": "pdf",
                    "type": {
                        "code": 0,
                        "name": "Не определено",
                        "signed": false
                    }
                },
                {
                    "id": 12150,
                    "fileName": "7841051711_Л-848_3.pdf",
                    "ext": "pdf",
                    "type": {
                        "code": 0,
                        "name": "Не определено",
                        "signed": false
                    }
                },
                {
                    "id": 12151,
                    "fileName": "7841051711_Л-848_4.pdf",
                    "ext": "pdf",
                    "type": {
                        "code": 0,
                        "name": "Не определено",
                        "signed": false
                    }
                },
                {
                    "id": 12152,
                    "fileName": "7841051711_Л-848_5.pdf",
                    "ext": "pdf",
                    "type": {
                        "code": 0,
                        "name": "Не определено",
                        "signed": false
                    }
                },
                {
                    "id": 12154,
                    "fileName": "7841051711_Л-848_7.pdf",
                    "ext": "pdf",
                    "type": {
                        "code": 0,
                        "name": "Не определено",
                        "signed": false
                    }
                },
                {
                    "id": 12149,
                    "fileName": "7841051711_Л-848_2.pdf",
                    "ext": "pdf",
                    "type": {
                        "code": 0,
                        "name": "Не определено",
                        "signed": false
                    }
                },
                {
                    "id": 12153,
                    "fileName": "7841051711_Л-848_6.pdf",
                    "ext": "pdf",
                    "type": {
                        "code": 0,
                        "name": "Не определено",
                        "signed": false
                    }
                }
            ],
            "regionCode": "78",
            "status": {
                "code": 2005,
                "description": "Приостановлено",
                "initialStatus": false,
                "finishedStatus": false,
                "requestResult": false
            },
            "indicator": {
                "finished": 12,
                "total": 26,
                "showPercent": true
            },
            "requestType": {
                "code": 7,
                "description": "Заявление о выдаче лицензии",
                "region": true
            },
            "reregTypes": null,
            "execUser": {
                "id": 103,
                "firstName": "Peter Petrovich",
                "middleName": null,
                "lastName": "Petrov"
            },
            "deliveryCode": 5,
            "finalResult": true,
            "rating": null,
            "newRegNum": null,
            "erulNumber": null,
            "suspensionSign": true,
            "indicationNum": null,
            "indicationColor": null,
            "statusCode": 2005,
            "description": "Приостановлено",
            "requestTypeDescription": "Заявление о выдаче лицензии",
            "licenseTypeId": 3,
            "requestTypeId": 7
        },
        {
            "requestId": 225390,
            "inn": "231909519706",
            "organization": "ИП МАНГРСУЗЯН С. А.",
            "orgBriefName": null,
            "orgFullName": null,
            "deloNum": "Л-842",
            "dateInsert": "2024-10-04T14:00:47.807",
            "dateChange": "2024-10-04T14:02:07.588613",
            "regNum": null,
            "deloDate": "2024-10-04",
            "regDate": null,
            "licenseType": {
                "code": 4,
                "description": "производство, хранение, поставки и розничная продажа произведенной сельскохозяйственными производителями винодельческой продукции",
                "shortName": "ПХПРП_СХП",
                "region": false
            },
            "attach": [
                {
                    "id": 12141,
                    "fileName": "231909519706_Л-842_1.pdf",
                    "ext": "pdf",
                    "type": {
                        "code": 0,
                        "name": "Не определено",
                        "signed": false
                    }
                },
                {
                    "id": 12142,
                    "fileName": "231909519706_Л-842_2.pdf",
                    "ext": "pdf",
                    "type": {
                        "code": 0,
                        "name": "Не определено",
                        "signed": false
                    }
                },
                {
                    "id": 12143,
                    "fileName": "231909519706_Л-842_3.pdf",
                    "ext": "pdf",
                    "type": {
                        "code": 0,
                        "name": "Не определено",
                        "signed": false
                    }
                },
                {
                    "id": 12144,
                    "fileName": "231909519706_Л-842_4.pdf",
                    "ext": "pdf",
                    "type": {
                        "code": 0,
                        "name": "Не определено",
                        "signed": false
                    }
                },
                {
                    "id": 12145,
                    "fileName": "231909519706_Л-842_5.pdf",
                    "ext": "pdf",
                    "type": {
                        "code": 0,
                        "name": "Не определено",
                        "signed": false
                    }
                },
                {
                    "id": 12146,
                    "fileName": "231909519706_Л-842_6.pdf",
                    "ext": "pdf",
                    "type": {
                        "code": 0,
                        "name": "Не определено",
                        "signed": false
                    }
                },
                {
                    "id": 12147,
                    "fileName": "231909519706_Л-842_7.pdf",
                    "ext": "pdf",
                    "type": {
                        "code": 0,
                        "name": "Не определено",
                        "signed": false
                    }
                }
            ],
            "regionCode": "23",
            "status": {
                "code": 2001,
                "description": "На рассмотрении",
                "initialStatus": true,
                "finishedStatus": false
            },
            "indicator": {
                "finished": 10,
                "total": 26,
                "showPercent": true
            },
            "requestType": {
                "code": 7,
                "description": "Заявление о выдаче лицензии",
                "region": true
            },
            "reregTypes": null,
            "execUser": {
                "id": 103,
                "firstName": "Peter Petrovich",
                "middleName": null,
                "lastName": "Petrov"
            },
            "deliveryCode": 5,
            "finalResult": true,
            "rating": null,
            "newRegNum": null,
            "erulNumber": null,
            "suspensionSign": false,
            "indicationNum": null,
            "indicationColor": null,
            "statusCode": 2001,
            "description": "На рассмотрении",
            "requestTypeDescription": "Заявление о выдаче лицензии",
            "licenseTypeId": 4,
            "requestTypeId": 7
        },
        {
            "requestId": 225389,
            "inn": "231909519706",
            "organization": "ИП МАНГРСУЗЯН С. А.",
            "orgBriefName": null,
            "orgFullName": null,
            "deloNum": "Л-840",
            "dateInsert": "2024-10-04T12:28:45.463",
            "dateChange": "2024-10-08T14:16:24.009581",
            "regNum": null,
            "deloDate": "2024-10-04",
            "regDate": null,
            "licenseType": {
                "code": 4,
                "description": "производство, хранение, поставки и розничная продажа произведенной сельскохозяйственными производителями винодельческой продукции",
                "shortName": "ПХПРП_СХП",
                "region": false
            },
            "attach": [
                {
                    "id": 12134,
                    "fileName": "231909519706_Л-840_1.pdf",
                    "ext": "pdf",
                    "type": {
                        "code": 0,
                        "name": "Не определено",
                        "signed": false
                    }
                },
                {
                    "id": 12135,
                    "fileName": "231909519706_Л-840_2.pdf",
                    "ext": "pdf",
                    "type": {
                        "code": 0,
                        "name": "Не определено",
                        "signed": false
                    }
                },
                {
                    "id": 12136,
                    "fileName": "231909519706_Л-840_3.pdf",
                    "ext": "pdf",
                    "type": {
                        "code": 0,
                        "name": "Не определено",
                        "signed": false
                    }
                },
                {
                    "id": 12137,
                    "fileName": "231909519706_Л-840_4.pdf",
                    "ext": "pdf",
                    "type": {
                        "code": 0,
                        "name": "Не определено",
                        "signed": false
                    }
                },
                {
                    "id": 12138,
                    "fileName": "231909519706_Л-840_5.pdf",
                    "ext": "pdf",
                    "type": {
                        "code": 0,
                        "name": "Не определено",
                        "signed": false
                    }
                },
                {
                    "id": 12139,
                    "fileName": "231909519706_Л-840_6.pdf",
                    "ext": "pdf",
                    "type": {
                        "code": 0,
                        "name": "Не определено",
                        "signed": false
                    }
                },
                {
                    "id": 12140,
                    "fileName": "231909519706_Л-840_7.pdf",
                    "ext": "pdf",
                    "type": {
                        "code": 0,
                        "name": "Не определено",
                        "signed": false
                    }
                }
            ],
            "regionCode": "23",
            "status": {
                "code": 2006,
                "description": "Ожидает приостановления",
                "initialStatus": false,
                "finishedStatus": false,
                "requestResult": false
            },
            "indicator": {
                "finished": 10,
                "total": 26,
                "showPercent": true
            },
            "requestType": {
                "code": 7,
                "description": "Заявление о выдаче лицензии",
                "region": true
            },
            "reregTypes": null,
            "execUser": {
                "id": 103,
                "firstName": "Peter Petrovich",
                "middleName": null,
                "lastName": "Petrov"
            },
            "deliveryCode": 5,
            "finalResult": true,
            "rating": null,
            "newRegNum": null,
            "erulNumber": null,
            "suspensionSign": false,
            "indicationNum": null,
            "indicationColor": null,
            "statusCode": 2006,
            "description": "Ожидает приостановления",
            "requestTypeDescription": "Заявление о выдаче лицензии",
            "licenseTypeId": 4,
            "requestTypeId": 7
        },
        {
            "requestId": 225361,
            "inn": "7841051711",
            "organization": "АО «ЦентрИнформ» ",
            "orgBriefName": null,
            "orgFullName": null,
            "deloNum": "Л-800",
            "dateInsert": "2024-09-30T15:29:27.883",
            "dateChange": "2024-09-30T15:31:58.784448",
            "regNum": null,
            "deloDate": "2024-09-30",
            "regDate": null,
            "licenseType": {
                "code": 3,
                "description": "производство, хранение и поставки произведенной сельскохозяйственными производителями винодельческой продукции",
                "shortName": "ПХП_СХП",
                "region": false
            },
            "attach": [
                {
                    "id": 12125,
                    "fileName": "7841051711_Л-800_2.pdf",
                    "ext": "pdf",
                    "type": {
                        "code": 0,
                        "name": "Не определено",
                        "signed": false
                    }
                },
                {
                    "id": 12126,
                    "fileName": "7841051711_Л-800_3.pdf",
                    "ext": "pdf",
                    "type": {
                        "code": 0,
                        "name": "Не определено",
                        "signed": false
                    }
                },
                {
                    "id": 12124,
                    "fileName": "7841051711_Л-800_1.pdf",
                    "ext": "pdf",
                    "type": {
                        "code": 0,
                        "name": "Не определено",
                        "signed": false
                    }
                },
                {
                    "id": 12129,
                    "fileName": "7841051711_Л-800_6.pdf",
                    "ext": "pdf",
                    "type": {
                        "code": 0,
                        "name": "Не определено",
                        "signed": false
                    }
                },
                {
                    "id": 12130,
                    "fileName": "7841051711_Л-800_7.pdf",
                    "ext": "pdf",
                    "type": {
                        "code": 0,
                        "name": "Не определено",
                        "signed": false
                    }
                },
                {
                    "id": 12131,
                    "fileName": "7841051711_Л-800_8.pdf",
                    "ext": "pdf",
                    "type": {
                        "code": 0,
                        "name": "Не определено",
                        "signed": false
                    }
                },
                {
                    "id": 12127,
                    "fileName": "7841051711_Л-800_4.pdf",
                    "ext": "pdf",
                    "type": {
                        "code": 0,
                        "name": "Не определено",
                        "signed": false
                    }
                },
                {
                    "id": 12128,
                    "fileName": "7841051711_Л-800_5.pdf",
                    "ext": "pdf",
                    "type": {
                        "code": 0,
                        "name": "Не определено",
                        "signed": false
                    }
                }
            ],
            "regionCode": "78",
            "status": {
                "code": 2001,
                "description": "На рассмотрении",
                "initialStatus": true,
                "finishedStatus": false
            },
            "indicator": {
                "finished": 11,
                "total": 26,
                "showPercent": true
            },
            "requestType": {
                "code": 7,
                "description": "Заявление о выдаче лицензии",
                "region": true
            },
            "reregTypes": null,
            "execUser": {
                "id": 121,
                "firstName": "Подрядчик",
                "middleName": null,
                "lastName": "АО 'ЦЕНТРИНФОРМ'"
            },
            "deliveryCode": 5,
            "finalResult": true,
            "rating": null,
            "newRegNum": null,
            "erulNumber": null,
            "suspensionSign": false,
            "indicationNum": null,
            "indicationColor": null,
            "statusCode": 2001,
            "description": "На рассмотрении",
            "requestTypeDescription": "Заявление о выдаче лицензии",
            "licenseTypeId": 3,
            "requestTypeId": 7
        },
        {
            "requestId": 225360,
            "inn": "7841051711",
            "organization": "АО «ЦентрИнформ» ",
            "orgBriefName": null,
            "orgFullName": null,
            "deloNum": "Л-799",
            "dateInsert": "2024-09-30T13:32:53.51",
            "dateChange": "2024-09-30T13:41:27.709014",
            "regNum": null,
            "deloDate": "2024-09-30",
            "regDate": null,
            "licenseType": {
                "code": 3,
                "description": "производство, хранение и поставки произведенной сельскохозяйственными производителями винодельческой продукции",
                "shortName": "ПХП_СХП",
                "region": false
            },
            "attach": [
                {
                    "id": 12117,
                    "fileName": "7841051711_Л-799_1.pdf",
                    "ext": "pdf",
                    "type": {
                        "code": 0,
                        "name": "Не определено",
                        "signed": false
                    }
                },
                {
                    "id": 12118,
                    "fileName": "7841051711_Л-799_2.pdf",
                    "ext": "pdf",
                    "type": {
                        "code": 0,
                        "name": "Не определено",
                        "signed": false
                    }
                },
                {
                    "id": 12119,
                    "fileName": "7841051711_Л-799_3.pdf",
                    "ext": "pdf",
                    "type": {
                        "code": 0,
                        "name": "Не определено",
                        "signed": false
                    }
                },
                {
                    "id": 12120,
                    "fileName": "7841051711_Л-799_4.pdf",
                    "ext": "pdf",
                    "type": {
                        "code": 0,
                        "name": "Не определено",
                        "signed": false
                    }
                },
                {
                    "id": 12121,
                    "fileName": "7841051711_Л-799_5.pdf",
                    "ext": "pdf",
                    "type": {
                        "code": 0,
                        "name": "Не определено",
                        "signed": false
                    }
                },
                {
                    "id": 12122,
                    "fileName": "7841051711_Л-799_6.pdf",
                    "ext": "pdf",
                    "type": {
                        "code": 0,
                        "name": "Не определено",
                        "signed": false
                    }
                },
                {
                    "id": 12123,
                    "fileName": "7841051711_Л-799_7.pdf",
                    "ext": "pdf",
                    "type": {
                        "code": 0,
                        "name": "Не определено",
                        "signed": false
                    }
                }
            ],
            "regionCode": "78",
            "status": {
                "code": 2001,
                "description": "На рассмотрении",
                "initialStatus": true,
                "finishedStatus": false
            },
            "indicator": {
                "finished": 13,
                "total": 26,
                "showPercent": true
            },
            "requestType": {
                "code": 7,
                "description": "Заявление о выдаче лицензии",
                "region": true
            },
            "reregTypes": null,
            "execUser": {
                "id": 121,
                "firstName": "Подрядчик",
                "middleName": null,
                "lastName": "АО 'ЦЕНТРИНФОРМ'"
            },
            "deliveryCode": 5,
            "finalResult": true,
            "rating": null,
            "newRegNum": null,
            "erulNumber": null,
            "suspensionSign": false,
            "indicationNum": null,
            "indicationColor": null,
            "statusCode": 2001,
            "description": "На рассмотрении",
            "requestTypeDescription": "Заявление о выдаче лицензии",
            "licenseTypeId": 3,
            "requestTypeId": 7
        },
        {
            "requestId": 225359,
            "inn": "7841051711",
            "organization": "АО «ЦентрИнформ» ",
            "orgBriefName": null,
            "orgFullName": null,
            "deloNum": "Л-798",
            "dateInsert": "2024-09-27T10:01:46.97",
            "dateChange": "2024-09-27T10:02:56.713377",
            "regNum": null,
            "deloDate": "2024-09-27",
            "regDate": null,
            "licenseType": {
                "code": 2,
                "description": "производство, хранение и поставки произведенной алкогольной продукции",
                "shortName": "ПХП_АП",
                "region": false
            },
            "attach": [
                {
                    "id": 12110,
                    "fileName": "7841051711_Л-798_2.pdf",
                    "ext": "pdf",
                    "type": {
                        "code": 0,
                        "name": "Не определено",
                        "signed": false
                    }
                },
                {
                    "id": 12111,
                    "fileName": "7841051711_Л-798_3.pdf",
                    "ext": "pdf",
                    "type": {
                        "code": 0,
                        "name": "Не определено",
                        "signed": false
                    }
                },
                {
                    "id": 12109,
                    "fileName": "7841051711_Л-798_1.pdf",
                    "ext": "pdf",
                    "type": {
                        "code": 0,
                        "name": "Не определено",
                        "signed": false
                    }
                },
                {
                    "id": 12112,
                    "fileName": "7841051711_Л-798_4.pdf",
                    "ext": "pdf",
                    "type": {
                        "code": 0,
                        "name": "Не определено",
                        "signed": false
                    }
                },
                {
                    "id": 12113,
                    "fileName": "7841051711_Л-798_5.pdf",
                    "ext": "pdf",
                    "type": {
                        "code": 0,
                        "name": "Не определено",
                        "signed": false
                    }
                },
                {
                    "id": 12115,
                    "fileName": "7841051711_Л-798_7.pdf",
                    "ext": "pdf",
                    "type": {
                        "code": 0,
                        "name": "Не определено",
                        "signed": false
                    }
                },
                {
                    "id": 12116,
                    "fileName": "7841051711_Л-798_8.pdf",
                    "ext": "pdf",
                    "type": {
                        "code": 0,
                        "name": "Не определено",
                        "signed": false
                    }
                },
                {
                    "id": 12114,
                    "fileName": "7841051711_Л-798_6.pdf",
                    "ext": "pdf",
                    "type": {
                        "code": 0,
                        "name": "Не определено",
                        "signed": false
                    }
                }
            ],
            "regionCode": "78",
            "status": {
                "code": 2001,
                "description": "На рассмотрении",
                "initialStatus": true,
                "finishedStatus": false
            },
            "indicator": {
                "finished": 12,
                "total": 22,
                "showPercent": true
            },
            "requestType": {
                "code": 7,
                "description": "Заявление о выдаче лицензии",
                "region": true
            },
            "reregTypes": null,
            "execUser": {
                "id": 103,
                "firstName": "Peter Petrovich",
                "middleName": null,
                "lastName": "Petrov"
            },
            "deliveryCode": 5,
            "finalResult": true,
            "rating": null,
            "newRegNum": null,
            "erulNumber": null,
            "suspensionSign": false,
            "indicationNum": null,
            "indicationColor": null,
            "statusCode": 2001,
            "description": "На рассмотрении",
            "requestTypeDescription": "Заявление о выдаче лицензии",
            "licenseTypeId": 2,
            "requestTypeId": 7
        },
        {
            "requestId": 225354,
            "inn": "7841051711",
            "organization": "АО «ЦентрИнформ» ",
            "orgBriefName": null,
            "orgFullName": null,
            "deloNum": "Л-796",
            "dateInsert": "2024-09-26T08:37:25.967",
            "dateChange": "2024-09-30T13:20:51.322934",
            "regNum": null,
            "deloDate": "2024-09-26",
            "regDate": null,
            "licenseType": {
                "code": 3,
                "description": "производство, хранение и поставки произведенной сельскохозяйственными производителями винодельческой продукции",
                "shortName": "ПХП_СХП",
                "region": false
            },
            "attach": [
                {
                    "id": 12097,
                    "fileName": "7841051711_Л-796_1.pdf",
                    "ext": "pdf",
                    "type": {
                        "code": 0,
                        "name": "Не определено",
                        "signed": false
                    }
                },
                {
                    "id": 12099,
                    "fileName": "7841051711_Л-796_3.pdf",
                    "ext": "pdf",
                    "type": {
                        "code": 0,
                        "name": "Не определено",
                        "signed": false
                    }
                },
                {
                    "id": 12100,
                    "fileName": "7841051711_Л-796_4.pdf",
                    "ext": "pdf",
                    "type": {
                        "code": 0,
                        "name": "Не определено",
                        "signed": false
                    }
                },
                {
                    "id": 12101,
                    "fileName": "7841051711_Л-796_5.pdf",
                    "ext": "pdf",
                    "type": {
                        "code": 0,
                        "name": "Не определено",
                        "signed": false
                    }
                },
                {
                    "id": 12102,
                    "fileName": "7841051711_Л-796_6.pdf",
                    "ext": "pdf",
                    "type": {
                        "code": 0,
                        "name": "Не определено",
                        "signed": false
                    }
                },
                {
                    "id": 12098,
                    "fileName": "7841051711_Л-796_2.pdf",
                    "ext": "pdf",
                    "type": {
                        "code": 0,
                        "name": "Не определено",
                        "signed": false
                    }
                },
                {
                    "id": 12103,
                    "fileName": "7841051711_Л-796_7.pdf",
                    "ext": "pdf",
                    "type": {
                        "code": 0,
                        "name": "Не определено",
                        "signed": false
                    }
                },
                {
                    "id": 12104,
                    "fileName": "7841051711_Л-796_8.pdf",
                    "ext": "pdf",
                    "type": {
                        "code": 0,
                        "name": "Не определено",
                        "signed": false
                    }
                }
            ],
            "regionCode": "78",
            "status": {
                "code": 2007,
                "description": "Ожидание отказа",
                "initialStatus": false,
                "finishedStatus": false,
                "requestResult": false
            },
            "indicator": {
                "finished": 6,
                "total": 26,
                "showPercent": true
            },
            "requestType": {
                "code": 7,
                "description": "Заявление о выдаче лицензии",
                "region": true
            },
            "reregTypes": null,
            "execUser": {
                "id": 121,
                "firstName": "Подрядчик",
                "middleName": null,
                "lastName": "АО 'ЦЕНТРИНФОРМ'"
            },
            "deliveryCode": 5,
            "finalResult": true,
            "rating": null,
            "newRegNum": null,
            "erulNumber": null,
            "suspensionSign": false,
            "indicationNum": null,
            "indicationColor": null,
            "statusCode": 2007,
            "description": "Ожидание отказа",
            "requestTypeDescription": "Заявление о выдаче лицензии",
            "licenseTypeId": 3,
            "requestTypeId": 7
        },
        {
            "requestId": 225352,
            "inn": "7841051711",
            "organization": "АО «ЦентрИнформ» ",
            "orgBriefName": null,
            "orgFullName": null,
            "deloNum": "Л-793",
            "dateInsert": "2024-09-25T10:52:59.23",
            "dateChange": "2024-09-25T11:04:51.447658",
            "regNum": null,
            "deloDate": "2024-09-25",
            "regDate": null,
            "licenseType": {
                "code": 3,
                "description": "производство, хранение и поставки произведенной сельскохозяйственными производителями винодельческой продукции",
                "shortName": "ПХП_СХП",
                "region": false
            },
            "attach": [
                {
                    "id": 12081,
                    "fileName": "7841051711_Л-793_1.pdf",
                    "ext": "pdf",
                    "type": {
                        "code": 0,
                        "name": "Не определено",
                        "signed": false
                    }
                },
                {
                    "id": 12082,
                    "fileName": "7841051711_Л-793_2.pdf",
                    "ext": "pdf",
                    "type": {
                        "code": 0,
                        "name": "Не определено",
                        "signed": false
                    }
                },
                {
                    "id": 12083,
                    "fileName": "7841051711_Л-793_3.pdf",
                    "ext": "pdf",
                    "type": {
                        "code": 0,
                        "name": "Не определено",
                        "signed": false
                    }
                },
                {
                    "id": 12084,
                    "fileName": "7841051711_Л-793_4.pdf",
                    "ext": "pdf",
                    "type": {
                        "code": 0,
                        "name": "Не определено",
                        "signed": false
                    }
                },
                {
                    "id": 12085,
                    "fileName": "7841051711_Л-793_5.pdf",
                    "ext": "pdf",
                    "type": {
                        "code": 0,
                        "name": "Не определено",
                        "signed": false
                    }
                },
                {
                    "id": 12086,
                    "fileName": "7841051711_Л-793_6.pdf",
                    "ext": "pdf",
                    "type": {
                        "code": 0,
                        "name": "Не определено",
                        "signed": false
                    }
                },
                {
                    "id": 12087,
                    "fileName": "7841051711_Л-793_7.pdf",
                    "ext": "pdf",
                    "type": {
                        "code": 0,
                        "name": "Не определено",
                        "signed": false
                    }
                },
                {
                    "id": 12088,
                    "fileName": "7841051711_Л-793_8.pdf",
                    "ext": "pdf",
                    "type": {
                        "code": 0,
                        "name": "Не определено",
                        "signed": false
                    }
                }
            ],
            "regionCode": "78",
            "status": {
                "code": 2001,
                "description": "На рассмотрении",
                "initialStatus": true,
                "finishedStatus": false
            },
            "indicator": {
                "finished": 12,
                "total": 26,
                "showPercent": true
            },
            "requestType": {
                "code": 7,
                "description": "Заявление о выдаче лицензии",
                "region": true
            },
            "reregTypes": null,
            "execUser": {
                "id": 121,
                "firstName": "Подрядчик",
                "middleName": null,
                "lastName": "АО 'ЦЕНТРИНФОРМ'"
            },
            "deliveryCode": 5,
            "finalResult": true,
            "rating": null,
            "newRegNum": null,
            "erulNumber": null,
            "suspensionSign": false,
            "indicationNum": null,
            "indicationColor": null,
            "statusCode": 2001,
            "description": "На рассмотрении",
            "requestTypeDescription": "Заявление о выдаче лицензии",
            "licenseTypeId": 3,
            "requestTypeId": 7
        },
        {
            "requestId": 225351,
            "inn": "7841051711",
            "organization": "АО «ЦентрИнформ» ",
            "orgBriefName": null,
            "orgFullName": null,
            "deloNum": "Л-792",
            "dateInsert": "2024-09-25T08:38:42.853",
            "dateChange": "2024-09-25T08:39:57.65685",
            "regNum": null,
            "deloDate": "2024-09-25",
            "regDate": null,
            "licenseType": {
                "code": 1,
                "description": "производство, хранение и поставки произведенного этилового спирта",
                "shortName": "ПХП_ЭС",
                "region": false
            },
            "attach": [
                {
                    "id": 12074,
                    "fileName": "7841051711_Л-792_2.pdf",
                    "ext": "pdf",
                    "type": {
                        "code": 0,
                        "name": "Не определено",
                        "signed": false
                    }
                },
                {
                    "id": 12075,
                    "fileName": "7841051711_Л-792_3.pdf",
                    "ext": "pdf",
                    "type": {
                        "code": 0,
                        "name": "Не определено",
                        "signed": false
                    }
                },
                {
                    "id": 12073,
                    "fileName": "7841051711_Л-792_1.pdf",
                    "ext": "pdf",
                    "type": {
                        "code": 0,
                        "name": "Не определено",
                        "signed": false
                    }
                },
                {
                    "id": 12076,
                    "fileName": "7841051711_Л-792_4.pdf",
                    "ext": "pdf",
                    "type": {
                        "code": 0,
                        "name": "Не определено",
                        "signed": false
                    }
                },
                {
                    "id": 12077,
                    "fileName": "7841051711_Л-792_5.pdf",
                    "ext": "pdf",
                    "type": {
                        "code": 0,
                        "name": "Не определено",
                        "signed": false
                    }
                },
                {
                    "id": 12079,
                    "fileName": "7841051711_Л-792_7.pdf",
                    "ext": "pdf",
                    "type": {
                        "code": 0,
                        "name": "Не определено",
                        "signed": false
                    }
                },
                {
                    "id": 12080,
                    "fileName": "7841051711_Л-792_8.pdf",
                    "ext": "pdf",
                    "type": {
                        "code": 0,
                        "name": "Не определено",
                        "signed": false
                    }
                },
                {
                    "id": 12078,
                    "fileName": "7841051711_Л-792_6.pdf",
                    "ext": "pdf",
                    "type": {
                        "code": 0,
                        "name": "Не определено",
                        "signed": false
                    }
                }
            ],
            "regionCode": "78",
            "status": {
                "code": 2001,
                "description": "На рассмотрении",
                "initialStatus": true,
                "finishedStatus": false
            },
            "indicator": {
                "finished": 13,
                "total": 22,
                "showPercent": true
            },
            "requestType": {
                "code": 7,
                "description": "Заявление о выдаче лицензии",
                "region": true
            },
            "reregTypes": null,
            "execUser": {
                "id": 121,
                "firstName": "Подрядчик",
                "middleName": null,
                "lastName": "АО 'ЦЕНТРИНФОРМ'"
            },
            "deliveryCode": 5,
            "finalResult": true,
            "rating": null,
            "newRegNum": null,
            "erulNumber": null,
            "suspensionSign": false,
            "indicationNum": null,
            "indicationColor": null,
            "statusCode": 2001,
            "description": "На рассмотрении",
            "requestTypeDescription": "Заявление о выдаче лицензии",
            "licenseTypeId": 1,
            "requestTypeId": 7
        },
        {
            "requestId": 225350,
            "inn": "7841051711",
            "organization": "АО «ЦентрИнформ» ",
            "orgBriefName": null,
            "orgFullName": null,
            "deloNum": "Л-791",
            "dateInsert": "2024-09-24T17:39:24.27",
            "dateChange": "2024-09-24T17:41:39.589594",
            "regNum": null,
            "deloDate": "2024-09-24",
            "regDate": null,
            "licenseType": {
                "code": 2,
                "description": "производство, хранение и поставки произведенной алкогольной продукции",
                "shortName": "ПХП_АП",
                "region": false
            },
            "attach": [
                {
                    "id": 12069,
                    "fileName": "7841051711_Л-791_1.pdf",
                    "ext": "pdf",
                    "type": {
                        "code": 0,
                        "name": "Не определено",
                        "signed": false
                    }
                },
                {
                    "id": 12070,
                    "fileName": "7841051711_Л-791_2.pdf",
                    "ext": "pdf",
                    "type": {
                        "code": 0,
                        "name": "Не определено",
                        "signed": false
                    }
                },
                {
                    "id": 12071,
                    "fileName": "7841051711_Л-791_3.pdf",
                    "ext": "pdf",
                    "type": {
                        "code": 0,
                        "name": "Не определено",
                        "signed": false
                    }
                },
                {
                    "id": 12072,
                    "fileName": "7841051711_Л-791_4.pdf",
                    "ext": "pdf",
                    "type": {
                        "code": 0,
                        "name": "Не определено",
                        "signed": false
                    }
                }
            ],
            "regionCode": "78",
            "status": {
                "code": 2001,
                "description": "На рассмотрении",
                "initialStatus": true,
                "finishedStatus": false
            },
            "indicator": {
                "finished": 13,
                "total": 22,
                "showPercent": true
            },
            "requestType": {
                "code": 7,
                "description": "Заявление о выдаче лицензии",
                "region": true
            },
            "reregTypes": null,
            "execUser": {
                "id": 103,
                "firstName": "Peter Petrovich",
                "middleName": null,
                "lastName": "Petrov"
            },
            "deliveryCode": 5,
            "finalResult": true,
            "rating": null,
            "newRegNum": null,
            "erulNumber": null,
            "suspensionSign": false,
            "indicationNum": null,
            "indicationColor": null,
            "statusCode": 2001,
            "description": "На рассмотрении",
            "requestTypeDescription": "Заявление о выдаче лицензии",
            "licenseTypeId": 2,
            "requestTypeId": 7
        }
    ],
    "pageable": {
        "sort": {
            "unsorted": false,
            "sorted": true,
            "empty": false
        },
        "offset": 0,
        "pageNumber": 0,
        "pageSize": 20,
        "paged": true,
        "unpaged": false
    },
    "totalPages": 20,
    "last": false,
    "totalElements": 389,
    "size": 20,
    "number": 0,
    "sort": {
        "unsorted": false,
        "sorted": true,
        "empty": false
    },
    "numberOfElements": 20,
    "first": true,
    "empty": false
}
</code></pre>
}}
<!-- #endregion --> 

<!-- #region(collapsed) [NAME] -->
{{collapse(Отрицательный фильтр код !=5)
<pre><code class='json'>
{
    "content": [
        {
            "requestId": 225418,
            "inn": "7841051711",
            "organization": "АО «ЦентрИнформ» ",
            "orgBriefName": null,
            "orgFullName": null,
            "deloNum": "Л-877",
            "dateInsert": "2024-10-09T13:13:44.06",
            "dateChange": "2024-10-09T13:16:07.872051",
            "regNum": null,
            "deloDate": "2024-10-09",
            "regDate": null,
            "licenseType": {
                "code": 8,
                "description": "закупка, хранение и поставки алкогольной продукции",
                "shortName": "ЗХП_АП",
                "region": false
            },
            "regionCode": "78",
            "status": {
                "code": 2001,
                "description": "На рассмотрении",
                "initialStatus": true,
                "finishedStatus": false
            },
            "indicator": {
                "finished": 3,
                "total": 21,
                "showPercent": true
            },
            "requestType": {
                "code": 7,
                "description": "Заявление о выдаче лицензии",
                "region": true
            },
            "reregTypes": null,
            "execUser": {
                "id": 103,
                "firstName": "Peter Petrovich",
                "middleName": null,
                "lastName": "Petrov"
            },
            "deliveryCode": 29,
            "finalResult": true,
            "rating": null,
            "newRegNum": null,
            "erulNumber": null,
            "suspensionSign": false,
            "indicationNum": null,
            "indicationColor": null,
            "statusCode": 2001,
            "description": "На рассмотрении",
            "requestTypeDescription": "Заявление о выдаче лицензии",
            "licenseTypeId": 8,
            "requestTypeId": 7
        },
        {
            "requestId": 225417,
            "inn": "7841051711",
            "organization": "АО «ЦентрИнформ» ",
            "orgBriefName": null,
            "orgFullName": null,
            "deloNum": "Л-876",
            "dateInsert": "2024-10-09T12:40:44.1",
            "dateChange": "2024-10-09T12:41:41.23132",
            "regNum": null,
            "deloDate": "2024-10-09",
            "regDate": null,
            "licenseType": {
                "code": 8,
                "description": "закупка, хранение и поставки алкогольной продукции",
                "shortName": "ЗХП_АП",
                "region": false
            },
            "regionCode": "78",
            "status": {
                "code": 2001,
                "description": "На рассмотрении",
                "initialStatus": true,
                "finishedStatus": false
            },
            "indicator": {
                "finished": 14,
                "total": 21,
                "showPercent": true
            },
            "requestType": {
                "code": 7,
                "description": "Заявление о выдаче лицензии",
                "region": true
            },
            "reregTypes": null,
            "execUser": {
                "id": 103,
                "firstName": "Peter Petrovich",
                "middleName": null,
                "lastName": "Petrov"
            },
            "deliveryCode": 29,
            "finalResult": true,
            "rating": null,
            "newRegNum": null,
            "erulNumber": null,
            "suspensionSign": false,
            "indicationNum": null,
            "indicationColor": null,
            "statusCode": 2001,
            "description": "На рассмотрении",
            "requestTypeDescription": "Заявление о выдаче лицензии",
            "licenseTypeId": 8,
            "requestTypeId": 7
        },
        {
            "requestId": 225416,
            "inn": "576853595470",
            "organization": "ИП Попова Д. А.",
            "orgBriefName": null,
            "orgFullName": null,
            "deloNum": "Л-875",
            "dateInsert": "2024-10-09T12:05:42.3",
            "dateChange": "2024-10-09T12:07:07.593036",
            "regNum": null,
            "deloDate": "2024-10-09",
            "regDate": null,
            "licenseType": {
                "code": 4,
                "description": "производство, хранение, поставки и розничная продажа произведенной сельскохозяйственными производителями винодельческой продукции",
                "shortName": "ПХПРП_СХП",
                "region": false
            },
            "regionCode": "57",
            "status": {
                "code": 2001,
                "description": "На рассмотрении",
                "initialStatus": true,
                "finishedStatus": false
            },
            "indicator": {
                "finished": 13,
                "total": 26,
                "showPercent": true
            },
            "requestType": {
                "code": 7,
                "description": "Заявление о выдаче лицензии",
                "region": true
            },
            "reregTypes": null,
            "execUser": {
                "id": 103,
                "firstName": "Peter Petrovich",
                "middleName": null,
                "lastName": "Petrov"
            },
            "deliveryCode": 29,
            "finalResult": true,
            "rating": null,
            "newRegNum": null,
            "erulNumber": null,
            "suspensionSign": false,
            "indicationNum": null,
            "indicationColor": null,
            "statusCode": 2001,
            "description": "На рассмотрении",
            "requestTypeDescription": "Заявление о выдаче лицензии",
            "licenseTypeId": 4,
            "requestTypeId": 7
        },
        {
            "requestId": 225414,
            "inn": "7841051711",
            "organization": "АО «ЦентрИнформ» ",
            "orgBriefName": null,
            "orgFullName": null,
            "deloNum": "Л-873",
            "dateInsert": "2024-10-08T18:54:31.383",
            "dateChange": "2024-10-08T18:55:37.176751",
            "regNum": null,
            "deloDate": "2024-10-08",
            "regDate": null,
            "licenseType": {
                "code": 8,
                "description": "закупка, хранение и поставки алкогольной продукции",
                "shortName": "ЗХП_АП",
                "region": false
            },
            "regionCode": "78",
            "status": {
                "code": 2001,
                "description": "На рассмотрении",
                "initialStatus": true,
                "finishedStatus": false
            },
            "indicator": {
                "finished": 12,
                "total": 21,
                "showPercent": true
            },
            "requestType": {
                "code": 7,
                "description": "Заявление о выдаче лицензии",
                "region": true
            },
            "reregTypes": null,
            "execUser": {
                "id": 121,
                "firstName": "Подрядчик",
                "middleName": null,
                "lastName": "АО 'ЦЕНТРИНФОРМ'"
            },
            "deliveryCode": 29,
            "finalResult": true,
            "rating": null,
            "newRegNum": null,
            "erulNumber": null,
            "suspensionSign": false,
            "indicationNum": null,
            "indicationColor": null,
            "statusCode": 2001,
            "description": "На рассмотрении",
            "requestTypeDescription": "Заявление о выдаче лицензии",
            "licenseTypeId": 8,
            "requestTypeId": 7
        },
        {
            "requestId": 225409,
            "inn": "7841051711",
            "organization": "АО «ЦентрИнформ» ",
            "orgBriefName": null,
            "orgFullName": null,
            "deloNum": "Л-867",
            "dateInsert": "2024-10-08T12:13:44.653",
            "dateChange": "2024-10-08T12:15:13.154459",
            "regNum": null,
            "deloDate": "2024-10-08",
            "regDate": null,
            "licenseType": {
                "code": 8,
                "description": "закупка, хранение и поставки алкогольной продукции",
                "shortName": "ЗХП_АП",
                "region": false
            },
            "regionCode": "78",
            "status": {
                "code": 2001,
                "description": "На рассмотрении",
                "initialStatus": true,
                "finishedStatus": false
            },
            "indicator": {
                "finished": 12,
                "total": 21,
                "showPercent": true
            },
            "requestType": {
                "code": 7,
                "description": "Заявление о выдаче лицензии",
                "region": true
            },
            "reregTypes": null,
            "execUser": {
                "id": 103,
                "firstName": "Peter Petrovich",
                "middleName": null,
                "lastName": "Petrov"
            },
            "deliveryCode": 29,
            "finalResult": true,
            "rating": null,
            "newRegNum": null,
            "erulNumber": null,
            "suspensionSign": false,
            "indicationNum": null,
            "indicationColor": null,
            "statusCode": 2001,
            "description": "На рассмотрении",
            "requestTypeDescription": "Заявление о выдаче лицензии",
            "licenseTypeId": 8,
            "requestTypeId": 7
        },
        {
            "requestId": 225408,
            "inn": "7841051711",
            "organization": "АО «ЦентрИнформ» ",
            "orgBriefName": null,
            "orgFullName": null,
            "deloNum": "Л-866",
            "dateInsert": "2024-10-08T11:18:02.043",
            "dateChange": "2024-10-08T11:20:11.379288",
            "regNum": null,
            "deloDate": "2024-10-08",
            "regDate": null,
            "licenseType": {
                "code": 8,
                "description": "закупка, хранение и поставки алкогольной продукции",
                "shortName": "ЗХП_АП",
                "region": false
            },
            "regionCode": "78",
            "status": {
                "code": 2001,
                "description": "На рассмотрении",
                "initialStatus": true,
                "finishedStatus": false
            },
            "indicator": {
                "finished": 12,
                "total": 21,
                "showPercent": true
            },
            "requestType": {
                "code": 7,
                "description": "Заявление о выдаче лицензии",
                "region": true
            },
            "reregTypes": null,
            "execUser": {
                "id": 103,
                "firstName": "Peter Petrovich",
                "middleName": null,
                "lastName": "Petrov"
            },
            "deliveryCode": 29,
            "finalResult": true,
            "rating": null,
            "newRegNum": null,
            "erulNumber": null,
            "suspensionSign": false,
            "indicationNum": null,
            "indicationColor": null,
            "statusCode": 2001,
            "description": "На рассмотрении",
            "requestTypeDescription": "Заявление о выдаче лицензии",
            "licenseTypeId": 8,
            "requestTypeId": 7
        },
        {
            "requestId": 225407,
            "inn": "7841051711",
            "organization": "АО «ЦентрИнформ» ",
            "orgBriefName": null,
            "orgFullName": null,
            "deloNum": "Л-865",
            "dateInsert": "2024-10-08T09:29:06",
            "dateChange": "2024-10-08T15:34:55.420084",
            "regNum": null,
            "deloDate": "2024-10-08",
            "regDate": null,
            "licenseType": {
                "code": 8,
                "description": "закупка, хранение и поставки алкогольной продукции",
                "shortName": "ЗХП_АП",
                "region": false
            },
            "regionCode": "78",
            "status": {
                "code": 2005,
                "description": "Приостановлено",
                "initialStatus": false,
                "finishedStatus": false,
                "requestResult": false
            },
            "indicator": {
                "finished": 12,
                "total": 21,
                "showPercent": true
            },
            "requestType": {
                "code": 7,
                "description": "Заявление о выдаче лицензии",
                "region": true
            },
            "reregTypes": null,
            "execUser": {
                "id": 103,
                "firstName": "Peter Petrovich",
                "middleName": null,
                "lastName": "Petrov"
            },
            "deliveryCode": 29,
            "finalResult": true,
            "rating": null,
            "newRegNum": null,
            "erulNumber": null,
            "suspensionSign": true,
            "indicationNum": null,
            "indicationColor": null,
            "statusCode": 2005,
            "description": "Приостановлено",
            "requestTypeDescription": "Заявление о выдаче лицензии",
            "licenseTypeId": 8,
            "requestTypeId": 7
        },
        {
            "requestId": 225404,
            "inn": "7841051711",
            "organization": "АО «ЦентрИнформ» ",
            "orgBriefName": null,
            "orgFullName": null,
            "deloNum": "Л-862",
            "dateInsert": "2024-10-07T16:35:52.74",
            "dateChange": "2024-10-07T16:36:32.843116",
            "regNum": null,
            "deloDate": "2024-10-07",
            "regDate": null,
            "licenseType": {
                "code": 8,
                "description": "закупка, хранение и поставки алкогольной продукции",
                "shortName": "ЗХП_АП",
                "region": false
            },
            "regionCode": "78",
            "status": {
                "code": 2001,
                "description": "На рассмотрении",
                "initialStatus": true,
                "finishedStatus": false
            },
            "indicator": {
                "finished": 3,
                "total": 21,
                "showPercent": true
            },
            "requestType": {
                "code": 7,
                "description": "Заявление о выдаче лицензии",
                "region": true
            },
            "reregTypes": null,
            "execUser": {
                "id": 124,
                "firstName": "Даниил Анатольевич",
                "middleName": null,
                "lastName": "Сагдиев"
            },
            "deliveryCode": 29,
            "finalResult": true,
            "rating": null,
            "newRegNum": null,
            "erulNumber": null,
            "suspensionSign": false,
            "indicationNum": null,
            "indicationColor": null,
            "statusCode": 2001,
            "description": "На рассмотрении",
            "requestTypeDescription": "Заявление о выдаче лицензии",
            "licenseTypeId": 8,
            "requestTypeId": 7
        },
        {
            "requestId": 225401,
            "inn": "7841051711",
            "organization": "АО «ЦентрИнформ» ",
            "orgBriefName": null,
            "orgFullName": null,
            "deloNum": "Л-857",
            "dateInsert": "2024-10-07T13:27:45.63",
            "dateChange": "2024-10-07T13:30:16.843544",
            "regNum": null,
            "deloDate": "2024-10-07",
            "regDate": null,
            "licenseType": {
                "code": 8,
                "description": "закупка, хранение и поставки алкогольной продукции",
                "shortName": "ЗХП_АП",
                "region": false
            },
            "regionCode": "78",
            "status": {
                "code": 2001,
                "description": "На рассмотрении",
                "initialStatus": true,
                "finishedStatus": false
            },
            "indicator": {
                "finished": 12,
                "total": 21,
                "showPercent": true
            },
            "requestType": {
                "code": 7,
                "description": "Заявление о выдаче лицензии",
                "region": true
            },
            "reregTypes": null,
            "execUser": {
                "id": 121,
                "firstName": "Подрядчик",
                "middleName": null,
                "lastName": "АО 'ЦЕНТРИНФОРМ'"
            },
            "deliveryCode": 29,
            "finalResult": true,
            "rating": null,
            "newRegNum": null,
            "erulNumber": null,
            "suspensionSign": false,
            "indicationNum": null,
            "indicationColor": null,
            "statusCode": 2001,
            "description": "На рассмотрении",
            "requestTypeDescription": "Заявление о выдаче лицензии",
            "licenseTypeId": 8,
            "requestTypeId": 7
        },
        {
            "requestId": 225400,
            "inn": "7841051711",
            "organization": "АО «ЦентрИнформ» ",
            "orgBriefName": null,
            "orgFullName": null,
            "deloNum": "Л-856",
            "dateInsert": "2024-10-07T13:27:15.723",
            "dateChange": "2024-10-07T14:10:36.0375",
            "regNum": null,
            "deloDate": "2024-10-07",
            "regDate": null,
            "licenseType": {
                "code": 8,
                "description": "закупка, хранение и поставки алкогольной продукции",
                "shortName": "ЗХП_АП",
                "region": false
            },
            "regionCode": "78",
            "status": {
                "code": 2005,
                "description": "Приостановлено",
                "initialStatus": false,
                "finishedStatus": false,
                "requestResult": false
            },
            "indicator": {
                "finished": 12,
                "total": 21,
                "showPercent": true
            },
            "requestType": {
                "code": 7,
                "description": "Заявление о выдаче лицензии",
                "region": true
            },
            "reregTypes": null,
            "execUser": {
                "id": 121,
                "firstName": "Подрядчик",
                "middleName": null,
                "lastName": "АО 'ЦЕНТРИНФОРМ'"
            },
            "deliveryCode": 29,
            "finalResult": true,
            "rating": null,
            "newRegNum": null,
            "erulNumber": null,
            "suspensionSign": true,
            "indicationNum": null,
            "indicationColor": null,
            "statusCode": 2005,
            "description": "Приостановлено",
            "requestTypeDescription": "Заявление о выдаче лицензии",
            "licenseTypeId": 8,
            "requestTypeId": 7
        },
        {
            "requestId": 225399,
            "inn": "7841051711",
            "organization": "АО «ЦентрИнформ» ",
            "orgBriefName": null,
            "orgFullName": null,
            "deloNum": "Л-855",
            "dateInsert": "2024-10-07T13:26:42.767",
            "dateChange": "2024-10-07T13:27:42.159739",
            "regNum": null,
            "deloDate": "2024-10-07",
            "regDate": null,
            "licenseType": {
                "code": 8,
                "description": "закупка, хранение и поставки алкогольной продукции",
                "shortName": "ЗХП_АП",
                "region": false
            },
            "regionCode": "78",
            "status": {
                "code": 2001,
                "description": "На рассмотрении",
                "initialStatus": true,
                "finishedStatus": false
            },
            "indicator": {
                "finished": 11,
                "total": 21,
                "showPercent": true
            },
            "requestType": {
                "code": 7,
                "description": "Заявление о выдаче лицензии",
                "region": true
            },
            "reregTypes": null,
            "execUser": {
                "id": 121,
                "firstName": "Подрядчик",
                "middleName": null,
                "lastName": "АО 'ЦЕНТРИНФОРМ'"
            },
            "deliveryCode": 29,
            "finalResult": true,
            "rating": null,
            "newRegNum": null,
            "erulNumber": null,
            "suspensionSign": false,
            "indicationNum": null,
            "indicationColor": null,
            "statusCode": 2001,
            "description": "На рассмотрении",
            "requestTypeDescription": "Заявление о выдаче лицензии",
            "licenseTypeId": 8,
            "requestTypeId": 7
        },
        {
            "requestId": 225397,
            "inn": "231909519706",
            "organization": "ИП МАНГРСУЗЯН С. А.",
            "orgBriefName": null,
            "orgFullName": null,
            "deloNum": "Л-850",
            "dateInsert": "2024-10-07T08:48:25.14",
            "dateChange": "2024-10-07T08:50:02.213937",
            "regNum": null,
            "deloDate": "2024-10-07",
            "regDate": null,
            "licenseType": {
                "code": 4,
                "description": "производство, хранение, поставки и розничная продажа произведенной сельскохозяйственными производителями винодельческой продукции",
                "shortName": "ПХПРП_СХП",
                "region": false
            },
            "regionCode": "23",
            "status": {
                "code": 2001,
                "description": "На рассмотрении",
                "initialStatus": true,
                "finishedStatus": false
            },
            "indicator": {
                "finished": 9,
                "total": 26,
                "showPercent": true
            },
            "requestType": {
                "code": 7,
                "description": "Заявление о выдаче лицензии",
                "region": true
            },
            "reregTypes": null,
            "execUser": {
                "id": 121,
                "firstName": "Подрядчик",
                "middleName": null,
                "lastName": "АО 'ЦЕНТРИНФОРМ'"
            },
            "deliveryCode": 29,
            "finalResult": true,
            "rating": null,
            "newRegNum": null,
            "erulNumber": null,
            "suspensionSign": false,
            "indicationNum": null,
            "indicationColor": null,
            "statusCode": 2001,
            "description": "На рассмотрении",
            "requestTypeDescription": "Заявление о выдаче лицензии",
            "licenseTypeId": 4,
            "requestTypeId": 7
        },
        {
            "requestId": 225396,
            "inn": "7841051711",
            "organization": "АО «ЦентрИнформ» ",
            "orgBriefName": null,
            "orgFullName": null,
            "deloNum": "Л-849",
            "dateInsert": "2024-10-06T18:01:17.83",
            "dateChange": "2024-10-07T13:22:53.516274",
            "regNum": null,
            "deloDate": "2024-10-06",
            "regDate": null,
            "licenseType": {
                "code": 8,
                "description": "закупка, хранение и поставки алкогольной продукции",
                "shortName": "ЗХП_АП",
                "region": false
            },
            "regionCode": "78",
            "status": {
                "code": 2007,
                "description": "Ожидание отказа",
                "initialStatus": false,
                "finishedStatus": false,
                "requestResult": false
            },
            "indicator": {
                "finished": 11,
                "total": 21,
                "showPercent": true
            },
            "requestType": {
                "code": 7,
                "description": "Заявление о выдаче лицензии",
                "region": true
            },
            "reregTypes": null,
            "execUser": {
                "id": 121,
                "firstName": "Подрядчик",
                "middleName": null,
                "lastName": "АО 'ЦЕНТРИНФОРМ'"
            },
            "deliveryCode": 29,
            "finalResult": true,
            "rating": null,
            "newRegNum": null,
            "erulNumber": null,
            "suspensionSign": false,
            "indicationNum": null,
            "indicationColor": null,
            "statusCode": 2007,
            "description": "Ожидание отказа",
            "requestTypeDescription": "Заявление о выдаче лицензии",
            "licenseTypeId": 8,
            "requestTypeId": 7
        },
        {
            "requestId": 225394,
            "inn": "7841051711",
            "organization": "АО «ЦентрИнформ» ",
            "orgBriefName": null,
            "orgFullName": null,
            "deloNum": "Л-847",
            "dateInsert": "2024-10-04T16:33:06.093",
            "dateChange": "2024-10-04T16:33:43.341137",
            "regNum": null,
            "deloDate": "2024-10-04",
            "regDate": null,
            "licenseType": {
                "code": 8,
                "description": "закупка, хранение и поставки алкогольной продукции",
                "shortName": "ЗХП_АП",
                "region": false
            },
            "regionCode": "78",
            "status": {
                "code": 2001,
                "description": "На рассмотрении",
                "initialStatus": true,
                "finishedStatus": false
            },
            "indicator": {
                "finished": 5,
                "total": 21,
                "showPercent": true
            },
            "requestType": {
                "code": 7,
                "description": "Заявление о выдаче лицензии",
                "region": true
            },
            "reregTypes": null,
            "execUser": {
                "id": 103,
                "firstName": "Peter Petrovich",
                "middleName": null,
                "lastName": "Petrov"
            },
            "deliveryCode": 29,
            "finalResult": true,
            "rating": null,
            "newRegNum": null,
            "erulNumber": null,
            "suspensionSign": false,
            "indicationNum": null,
            "indicationColor": null,
            "statusCode": 2001,
            "description": "На рассмотрении",
            "requestTypeDescription": "Заявление о выдаче лицензии",
            "licenseTypeId": 8,
            "requestTypeId": 7
        },
        {
            "requestId": 225393,
            "inn": "771510315518",
            "organization": "Крестьянское (фермерское) хозяйство Козлакова Екатерина Васильевна",
            "orgBriefName": null,
            "orgFullName": null,
            "deloNum": "Л-846",
            "dateInsert": "2024-10-04T16:32:25.83",
            "dateChange": "2024-10-04T16:33:43.300615",
            "regNum": null,
            "deloDate": "2024-10-04",
            "regDate": null,
            "licenseType": {
                "code": 4,
                "description": "производство, хранение, поставки и розничная продажа произведенной сельскохозяйственными производителями винодельческой продукции",
                "shortName": "ПХПРП_СХП",
                "region": false
            },
            "regionCode": "77",
            "status": {
                "code": 2001,
                "description": "На рассмотрении",
                "initialStatus": true,
                "finishedStatus": false
            },
            "indicator": {
                "finished": 9,
                "total": 26,
                "showPercent": true
            },
            "requestType": {
                "code": 7,
                "description": "Заявление о выдаче лицензии",
                "region": true
            },
            "reregTypes": null,
            "execUser": {
                "id": 103,
                "firstName": "Peter Petrovich",
                "middleName": null,
                "lastName": "Petrov"
            },
            "deliveryCode": 29,
            "finalResult": true,
            "rating": null,
            "newRegNum": null,
            "erulNumber": null,
            "suspensionSign": false,
            "indicationNum": null,
            "indicationColor": null,
            "statusCode": 2001,
            "description": "На рассмотрении",
            "requestTypeDescription": "Заявление о выдаче лицензии",
            "licenseTypeId": 4,
            "requestTypeId": 7
        },
        {
            "requestId": 225392,
            "inn": "231909519706",
            "organization": "ИП МАНГРСУЗЯН С. А.",
            "orgBriefName": null,
            "orgFullName": null,
            "deloNum": "Л-845",
            "dateInsert": "2024-10-04T15:10:04.38",
            "dateChange": "2024-10-04T15:11:07.55812",
            "regNum": null,
            "deloDate": "2024-10-04",
            "regDate": null,
            "licenseType": {
                "code": 4,
                "description": "производство, хранение, поставки и розничная продажа произведенной сельскохозяйственными производителями винодельческой продукции",
                "shortName": "ПХПРП_СХП",
                "region": false
            },
            "regionCode": "23",
            "status": {
                "code": 2001,
                "description": "На рассмотрении",
                "initialStatus": true,
                "finishedStatus": false
            },
            "indicator": {
                "finished": 9,
                "total": 26,
                "showPercent": true
            },
            "requestType": {
                "code": 7,
                "description": "Заявление о выдаче лицензии",
                "region": true
            },
            "reregTypes": null,
            "execUser": {
                "id": 103,
                "firstName": "Peter Petrovich",
                "middleName": null,
                "lastName": "Petrov"
            },
            "deliveryCode": 29,
            "finalResult": true,
            "rating": null,
            "newRegNum": null,
            "erulNumber": null,
            "suspensionSign": false,
            "indicationNum": null,
            "indicationColor": null,
            "statusCode": 2001,
            "description": "На рассмотрении",
            "requestTypeDescription": "Заявление о выдаче лицензии",
            "licenseTypeId": 4,
            "requestTypeId": 7
        },
        {
            "requestId": 225391,
            "inn": "231909519706",
            "organization": "ИП МАНГРСУЗЯН С. А.",
            "orgBriefName": null,
            "orgFullName": null,
            "deloNum": "Л-844",
            "dateInsert": "2024-10-04T15:07:09.457",
            "dateChange": "2024-10-04T15:08:33.616431",
            "regNum": null,
            "deloDate": "2024-10-04",
            "regDate": null,
            "licenseType": {
                "code": 8,
                "description": "закупка, хранение и поставки алкогольной продукции",
                "shortName": "ЗХП_АП",
                "region": false
            },
            "regionCode": "23",
            "status": {
                "code": 2001,
                "description": "На рассмотрении",
                "initialStatus": true,
                "finishedStatus": false
            },
            "indicator": {
                "finished": 0,
                "total": 21,
                "showPercent": false
            },
            "requestType": {
                "code": 7,
                "description": "Заявление о выдаче лицензии",
                "region": true
            },
            "reregTypes": null,
            "execUser": {
                "id": 103,
                "firstName": "Peter Petrovich",
                "middleName": null,
                "lastName": "Petrov"
            },
            "deliveryCode": 29,
            "finalResult": true,
            "rating": null,
            "newRegNum": null,
            "erulNumber": null,
            "suspensionSign": false,
            "indicationNum": null,
            "indicationColor": null,
            "statusCode": 2001,
            "description": "На рассмотрении",
            "requestTypeDescription": "Заявление о выдаче лицензии",
            "licenseTypeId": 8,
            "requestTypeId": 7
        },
        {
            "requestId": 225388,
            "inn": "7841051711",
            "organization": "АО «ЦентрИнформ» ",
            "orgBriefName": null,
            "orgFullName": null,
            "deloNum": "Л-833",
            "dateInsert": "2024-10-04T11:31:11.907",
            "dateChange": "2024-10-04T11:32:37.498487",
            "regNum": null,
            "deloDate": "2024-10-04",
            "regDate": null,
            "licenseType": {
                "code": 8,
                "description": "закупка, хранение и поставки алкогольной продукции",
                "shortName": "ЗХП_АП",
                "region": false
            },
            "regionCode": "78",
            "status": {
                "code": 2001,
                "description": "На рассмотрении",
                "initialStatus": true,
                "finishedStatus": false
            },
            "indicator": {
                "finished": 12,
                "total": 21,
                "showPercent": true
            },
            "requestType": {
                "code": 7,
                "description": "Заявление о выдаче лицензии",
                "region": true
            },
            "reregTypes": null,
            "execUser": {
                "id": 103,
                "firstName": "Peter Petrovich",
                "middleName": null,
                "lastName": "Petrov"
            },
            "deliveryCode": 29,
            "finalResult": true,
            "rating": null,
            "newRegNum": null,
            "erulNumber": null,
            "suspensionSign": false,
            "indicationNum": null,
            "indicationColor": null,
            "statusCode": 2001,
            "description": "На рассмотрении",
            "requestTypeDescription": "Заявление о выдаче лицензии",
            "licenseTypeId": 8,
            "requestTypeId": 7
        },
        {
            "requestId": 225387,
            "inn": "7841051711",
            "organization": "АО «ЦентрИнформ» ",
            "orgBriefName": null,
            "orgFullName": null,
            "deloNum": "Л-832",
            "dateInsert": "2024-10-04T11:30:43.303",
            "dateChange": "2024-10-04T11:32:37.481303",
            "regNum": null,
            "deloDate": "2024-10-04",
            "regDate": null,
            "licenseType": {
                "code": 8,
                "description": "закупка, хранение и поставки алкогольной продукции",
                "shortName": "ЗХП_АП",
                "region": false
            },
            "regionCode": "78",
            "status": {
                "code": 2001,
                "description": "На рассмотрении",
                "initialStatus": true,
                "finishedStatus": false
            },
            "indicator": {
                "finished": 12,
                "total": 21,
                "showPercent": true
            },
            "requestType": {
                "code": 7,
                "description": "Заявление о выдаче лицензии",
                "region": true
            },
            "reregTypes": null,
            "execUser": {
                "id": 103,
                "firstName": "Peter Petrovich",
                "middleName": null,
                "lastName": "Petrov"
            },
            "deliveryCode": 29,
            "finalResult": true,
            "rating": null,
            "newRegNum": null,
            "erulNumber": null,
            "suspensionSign": false,
            "indicationNum": null,
            "indicationColor": null,
            "statusCode": 2001,
            "description": "На рассмотрении",
            "requestTypeDescription": "Заявление о выдаче лицензии",
            "licenseTypeId": 8,
            "requestTypeId": 7
        },
        {
            "requestId": 225386,
            "inn": "7841051711",
            "organization": "АО «ЦентрИнформ» ",
            "orgBriefName": null,
            "orgFullName": null,
            "deloNum": "Л-830",
            "dateInsert": "2024-10-04T11:30:14.247",
            "dateChange": "2024-10-04T11:32:37.456371",
            "regNum": null,
            "deloDate": "2024-10-04",
            "regDate": null,
            "licenseType": {
                "code": 8,
                "description": "закупка, хранение и поставки алкогольной продукции",
                "shortName": "ЗХП_АП",
                "region": false
            },
            "regionCode": "78",
            "status": {
                "code": 2001,
                "description": "На рассмотрении",
                "initialStatus": true,
                "finishedStatus": false
            },
            "indicator": {
                "finished": 10,
                "total": 21,
                "showPercent": true
            },
            "requestType": {
                "code": 7,
                "description": "Заявление о выдаче лицензии",
                "region": true
            },
            "reregTypes": null,
            "execUser": {
                "id": 103,
                "firstName": "Peter Petrovich",
                "middleName": null,
                "lastName": "Petrov"
            },
            "deliveryCode": 29,
            "finalResult": true,
            "rating": null,
            "newRegNum": null,
            "erulNumber": null,
            "suspensionSign": false,
            "indicationNum": null,
            "indicationColor": null,
            "statusCode": 2001,
            "description": "На рассмотрении",
            "requestTypeDescription": "Заявление о выдаче лицензии",
            "licenseTypeId": 8,
            "requestTypeId": 7
        }
    ],
    "pageable": {
        "sort": {
            "unsorted": false,
            "sorted": true,
            "empty": false
        },
        "offset": 0,
        "pageNumber": 0,
        "pageSize": 20,
        "paged": true,
        "unpaged": false
    },
    "totalPages": 80,
    "last": false,
    "totalElements": 1587,
    "size": 20,
    "number": 0,
    "sort": {
        "unsorted": false,
        "sorted": true,
        "empty": false
    },
    "numberOfElements": 20,
    "first": true,
    "empty": false
}
</code></pre>
}}
<!-- #endregion --> 
%{color:green}При положительном отображаются только заявления с ЕПГУ , при отрицательном все, кроме заявлений с ЕПГУ%