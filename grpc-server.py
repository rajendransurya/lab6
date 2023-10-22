from concurrent import futures
import logging
import grpc
import grpc_rest_pb2
import grpc_rest_pb2_grpc
import io
from PIL import Image
import traceback
import base64

class Grpc_lab6Servicer(grpc_rest_pb2_grpc.Grpc_lab6Servicer):
        def PerformAdd(self, request, context):
            sum = request.a + request.b
            return grpc_rest_pb2.addReply(sum=sum)

        def ImageDimensions(self, request, context):
            # convert the data to a PIL image type so we can extract dimensions
            try:
                ioBuffer = io.BytesIO(request.img)
                img = Image.open(ioBuffer)
                return grpc_rest_pb2.imageReply(width=img.size[0], height=img.size[1])
            except:
                traceback.print_exc()
                return grpc_rest_pb2.imageReply(width=0, height=0)

        def PerformDotProduct(self, request, context):
            if request.a is None or request.b is None or len(request.a) != len(request.b):
                print('Invalid Input. Please Check and try again')
                return grpc_rest_pb2.dotProductReply(dotproduct=0)

            sum = 0
            for i in range(len(request.a)):
                sum += request.a[i] * request.b[i]

            return grpc_rest_pb2.dotProductReply(dotproduct=sum)

        def JsonImageDimensions(self, request, context):
            try:
                ioBuffer = io.BytesIO(base64.b64decode(request.img))
                img = Image.open(ioBuffer)
                return grpc_rest_pb2.imageReply(width=img.size[0], height=img.size[1])
            except:
                traceback.print_exc()
                return grpc_rest_pb2.imageReply(width=0, height=0)
def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    grpc_rest_pb2_grpc.add_Grpc_lab6Servicer_to_server(Grpc_lab6Servicer(), server)
    server.add_insecure_port('[::]:5000')
    server.start()
    print("Server started, listening on 5000")
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()
