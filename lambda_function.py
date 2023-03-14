import boto3
s3_client=boto3.client("s3")

dynamodb=boto3.resource('dynamodb')
table=dynamodb.Table('funcionarios')
def lambda_handler(event, context):
    bucket_name = event['Records'][0]['s3']['bucket']['name']
    s3_file_name = event['Records'][0]['s3']['object']['key']
    resp=s3_client.get_object(Bucket=bucket_name, Key=s3_file_name)
    data=resp['Body'].read().decode("utf-8")
    cadastro_usuarios=data.split("\n")
    for cadastro in cadastro_usuarios:
        print(cadastro)
        cadastro_dados = cadastro.split(",")
        try:
            table.put_item(
            Item = {"id":cadastro_dados[0],"name": cadastro_dados[1],"cpf/cnpj": cadastro_dados[2]}
                )
        except Exception as e:
            print("End of file")
