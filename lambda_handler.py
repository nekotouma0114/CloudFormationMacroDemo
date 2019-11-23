import json

def lambda_handler(event, context):
    #今回の許可ポート対象
    allow_ports = (80,443)
    """
    NOTE: paramsの想定値
        event['params'] = {
            'description': 'sg description(全て共通)'
            'cidr_list': [
                'x.x.x.x/x',
                'y.y.y.y/y'
            ]
        }
    """
    print(event)
    if 'cidr_list' not in event['params'] or 'description' not in event['params']:
        #本当はしっかりしたパラメータを返した方がいい気がするけどエラーになることは変わりないので適当に返す
        return

    #responseの外形を生成
    response = {
        'requestId': event['requestId'],
        'status': 'success',
        'fragment': []
    }

    #内容物を生成
    for cidr in event['params']['cidr_list']:
        for allow_port in allow_ports:
            response['fragment'].append(generate_sg(cidr,event['params']['description'],allow_port))
    return response

#ログ出力用のデコレーターを作る予定
def generate_sg(cidr: str,description: str,port: int) -> dict:
    """
        Security GroupのSecurityGroupIngressに設定する単一の設定を返却する
        Protcolはべた書きでTPCのみ対応。
        Portも範囲指定は未対応
    """
    return {
        'Description': description,
        'IpProtocol': 'tcp',
        'FromPort': port,
        'ToPort': port,
        'CidrIp': cidr
    }

#検証用。ほんとはテストコードをしっかり書いてネ
if __name__ == '__main__':
    event = dict()
    #コードで必要なもののみ抜粋本当はもっといろんなパラメータがある
    event['requestId'] = '1111'
    event['params'] = {
        'description': 'descrition',
        'cidr_list': ['192.168.2.1/32','192.168.2.2/32']
    }
    print(lambda_handler(event,""))
