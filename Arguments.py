"""
Arguments
"""
import boto3

def translate_text(text, source_language_code, target_language_code): # we define the positional arguments in the ()
    client = boto3.client('translate')
    response = client.translate_text(
        Text=text,
        SourceLanguageCode=source_language_code, #used a positional argument instead 
        TargetLanguageCode=target_language_code 
    )
    print(response) 

def main():
    translate_text('I am learning to code in AWS', 'en', 'fr')

if __name__=="__main__":
    main()


#Python substituted the actual values we provided when we called the function for the positional arguments and passed them to the parameters
#By removing the hard coded values we can now call the function multiple times using different values. This makes our code flexible and reusable.
