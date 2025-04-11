import boto3

    ec2 = boto3.client('ec2', region_name='us-east-1')  

        response = ec2.run_instances(
            ImageId='ami-0abcdef1234567890',  
            InstanceType='t2.micro',
            KeyName='windows',    
            MinCount=1,
            MaxCount=1,
