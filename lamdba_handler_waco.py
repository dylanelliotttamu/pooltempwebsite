# lambda handler file for Waco Wave Pool Temperature Forecast


# Read in the data from the text file
with open('data.txt', 'r') as file:
    data = file.read()

print(data)


def lambda_handler(event, context):
    
    body = f'''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Waco Wave Pool Temperature Forecast</title>
    </head>
    <body>
        <h1>Waco Wave Pool Temperature Forecast</h1>
        
        <p>Welcome to the Waco Wave Pool temperature forecast page! Here, you will find the latest updates on the temperature conditions at the Waco wave pool, ensuring you have the perfect day for surfing and fun.</p>
        
        <h2>Today's Forecast</h2>
        <p>The current temperature at the wave pool is <strong>80°F</strong> with a slight breeze making it a perfect day to catch some waves!</p>
        
        <h2>Weekly Forecast</h2>
        <ul>
            <li>Monday: 78°F, sunny</li>
            <li>Tuesday: 80°F, partly cloudy</li>
            <li>Wednesday: 82°F, sunny</li>
            <li>Thursday: 79°F, sunny</li>
            <li>Friday: 81°F, partly cloudy</li>
            <li>Saturday: 83°F, sunny</li>
            <li>Sunday: {data}°F, sunny</li>
        </ul>
        
        <img src="https://example.com/waco-wave-pool.jpg" alt="Waco Wave Pool" width="500" />
        
        <p>Stay tuned for more updates and enjoy your time at the Waco wave pool!</p>
        <p>For more details and updates, check out our <a href='/default/blog'>blog</a>.</p>
    </body>
    </html>
    '''
        
    response = {
        'statusCode': 200,
        'headers': {"Content-Type": "text/html"},
        'body': body
    }
    
    return response