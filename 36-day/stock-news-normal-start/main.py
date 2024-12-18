import requests
from twilio.rest import Client
STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
STOCK_API_KEY=STOCK_API_KEY
NEWS_API_KEY=NEWS_API_KEY
account_sid="id"
auth_token="token"

## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

parameter={
    "function":"TIME_SERIES_DAILY",
    "symbol":STOCK_NAME,
    "apikey":STOCK_API_KEY
}
stocks_data=requests.get(STOCK_ENDPOINT,params=parameter)
stocks_data.raise_for_status()
data=stocks_data.json()['Time Series (Daily)']
print(data)
#TODO 1. - Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g. [new_value for (key, value) in dictionary.items()]
yesterday_stocks=float([value for (key,value) in data.items()][0]['4. close'])
yesterday_stocks_date=[key for (key,_) in data.items()][0]
print(yesterday_stocks_date)
print(yesterday_stocks)

#TODO 2. - Get the day before yesterday's closing stock price
day_before_yest_stocks=float([value for (key,value) in data.items()][1]['4. close'])
day_before_yest_stocks_date=[key for (key,_) in data.items()][1]
print(day_before_yest_stocks_date)
print(day_before_yest_stocks)

#TODO 3. - Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp
difference=yesterday_stocks-day_before_yest_stocks
up_down=None
if difference >0:
    up_down="🔼"
else:
    up_down="🔽"
print(difference)

#TODO 4. - Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.
Percentage=round((difference / yesterday_stocks) * 100)
print(Percentage)

#TODO 5. - If TODO4 percentage is greater than 5 then print("Get News").
news_parameter={
    "qInTitle":COMPANY_NAME,
    "apiKey":NEWS_API_KEY
}
if abs(Percentage) <5:
    print("Get News")
    news=requests.get(NEWS_ENDPOINT,params=news_parameter)
    news.raise_for_status()
    data=news.json()['articles']
    print(data)
    ## STEP 2: https://newsapi.org/ 
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 


#TODO 6. - Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.

#TODO 7. - Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation
    first_three=data[:3]
    print(first_three)

    ## STEP 3: Use twilio.com/docs/sms/quickstart/python
    #to send a separate message with each article's title and description to your phone number. 

#TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.

    combine = [{"title":article['title'],"description":article['description']} for article in first_three]
    print(combine)
#TODO 9. - Send each article as a separate message via Twilio. 
    client = Client(account_sid, auth_token)
    for index in range(len(combine)):
        message = client.messages \
            .create(
            body=f"{STOCK_NAME} : {up_down} {Percentage} % Headline: {combine[index]['title']}\n Brief: {combine[index]['description']}",
            from_="your_twillio_phone_number",
            to="your_friend_number"
        )
        print(message.status)


#Optional TODO: Format the message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

