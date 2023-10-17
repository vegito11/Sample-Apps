from flask import Blueprint, jsonify, request

from data.utils import list_bucket_objects, get_ssm_parameter

aws_controller = Blueprint('aws_controller', __name__)


@aws_controller.route('/aws/bucket/<bkt_name>', methods=['GET'])
def list_s3_objects(bkt_name):
    
    try:
        response = list_bucket_objects(bkt_name)
        return jsonify({"S3 Objects": response})
    except Exception as e:
        return jsonify({"error": str(e)})


@aws_controller.route('/aws/param/<path:param_nm>', methods=['GET'])
def get_parameter(param_nm):
    print(param_nm)
    try:
        parameter_value  = get_ssm_parameter(f'/{param_nm}')
        return jsonify({param_nm: parameter_value })
    except Exception as e:
        return jsonify({"error": str(e)})

# http://127.0.0.1:5000/aws/bucket/cf-templates-1s2o42js6oxs2-us-east-1
# http://127.0.0.1:5000/aws/param/dev/username