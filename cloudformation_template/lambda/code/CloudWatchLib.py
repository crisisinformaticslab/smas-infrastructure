import boto3                                                                     

cloudwatch = boto3.client('cloudwatch')                                          

def create_alarm(term):                                                  
    cloudwatch.put_metric_alarm(                                                    
        AlarmName='{}_tweet_volume'.format(term),                                   
        AlarmDescription='Less than 5 tweets in 24 hours',                          
        MetricName='IngestionCount',                                                
        Namespace='twitter-ingestion-works',                                        
        ComparisonOperator='LessThanThreshold',                                     
        EvaluationPeriods=1,                                                        
        Period=86400,                                                               
        Statistic='Sum',                                                            
        Threshold=10,                                                            
        ActionsEnabled=True,                                                        
        AlarmActions=['arn:aws:sns:us-west-2:330520437911:search_term_deletion'],
        Dimensions=[                                                             
            {'Value': term, 'Name': 'term'}                                      
        ]                                                                        
    )
    
    
def delete_alarms(term_list):                                                    
    for t in term_list:                                                          
        cloudwatch.delete_alarms(                                                
            AlarmNames=['{}_tweet_volume'.format(t)]                                                    
        )                                                                        
