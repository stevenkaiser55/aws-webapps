const AWS = require('aws-sdk');

var s3 = new AWS.S3();
exports.handler = (event, context, callback) => {
     let encodedImage =JSON.parse(event.body).user_avatar;
     let decodedImage = Buffer.from(encodedImage, 'base64');
     var filePath = "profile_photo/" + event.queryStringParameters.name + ".jpg"
     var params = {
       "Body": decodedImage,
       "Bucket": "cfs3-webapps-business-card-profilephoto-qlzhysz7y6mb",
       "Key": filePath  
    };
    s3.upload(params, function(err, data){
       if(err) {
           callback(err, null);
       } else {
           let response = {
        "statusCode": 200,
        "headers": {
            "my_header": "my_value"
        },
        "body": JSON.stringify(data),
        "isBase64Encoded": false
    };
           callback(null, response);
    }
    });
    
};