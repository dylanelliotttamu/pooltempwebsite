# original lambda handler for example 

def lambda_handler(event, context):
    
    body = '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Homepage</title>
    </head>
    <body>
        <h1>Wave Pool Temperature Forecast</h1>
        
        <p>Hi! My name is Dylan Elliott. I'm a graduate research assistnat at Texas A&M University.  
        I am passionate about solving atmospheric and ocean science problems through programming and devoloping practial solutions to our real world problems.</p>
        <img src="https://example.com/your-image.jpg" alt="Dylan Elliott" width="500" />
        <p>Feel free to explore my blog for insights into my research and projects.</p>
        <p>Check out my <a href='/default/blog'>blog</a>.</p>
    </body>
    </html>
    '''
        
    response = {
        'statusCode': 200,
        'headers': {"Content-Type": "text/html",},
        'body': body
    }
    
    return response