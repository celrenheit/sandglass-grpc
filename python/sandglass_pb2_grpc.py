# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import sandglass_pb2 as sandglass__pb2


class BrokerServiceStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.CreateTopic = channel.unary_unary(
        '/sandglass.BrokerService/CreateTopic',
        request_serializer=sandglass__pb2.CreateTopicParams.SerializeToString,
        response_deserializer=sandglass__pb2.TopicReply.FromString,
        )
    self.GetTopic = channel.unary_unary(
        '/sandglass.BrokerService/GetTopic',
        request_serializer=sandglass__pb2.GetTopicParams.SerializeToString,
        response_deserializer=sandglass__pb2.GetTopicReply.FromString,
        )
    self.Produce = channel.unary_unary(
        '/sandglass.BrokerService/Produce',
        request_serializer=sandglass__pb2.ProduceMessageRequest.SerializeToString,
        response_deserializer=sandglass__pb2.ProduceResponse.FromString,
        )
    self.ProduceMessagesStream = channel.stream_unary(
        '/sandglass.BrokerService/ProduceMessagesStream',
        request_serializer=sandglass__pb2.Message.SerializeToString,
        response_deserializer=sandglass__pb2.StoreLocallyReply.FromString,
        )
    self.FetchFrom = channel.unary_stream(
        '/sandglass.BrokerService/FetchFrom',
        request_serializer=sandglass__pb2.FetchFromRequest.SerializeToString,
        response_deserializer=sandglass__pb2.Message.FromString,
        )
    self.FetchRange = channel.unary_stream(
        '/sandglass.BrokerService/FetchRange',
        request_serializer=sandglass__pb2.FetchRangeRequest.SerializeToString,
        response_deserializer=sandglass__pb2.Message.FromString,
        )
    self.ConsumeFromGroup = channel.unary_stream(
        '/sandglass.BrokerService/ConsumeFromGroup',
        request_serializer=sandglass__pb2.ConsumeFromGroupRequest.SerializeToString,
        response_deserializer=sandglass__pb2.Message.FromString,
        )
    self.Acknowledge = channel.unary_unary(
        '/sandglass.BrokerService/Acknowledge',
        request_serializer=sandglass__pb2.OffsetChangeRequest.SerializeToString,
        response_deserializer=sandglass__pb2.OffsetChangeReply.FromString,
        )
    self.AcknowledgeMessages = channel.unary_unary(
        '/sandglass.BrokerService/AcknowledgeMessages',
        request_serializer=sandglass__pb2.MultiOffsetChangeRequest.SerializeToString,
        response_deserializer=sandglass__pb2.OffsetChangeReply.FromString,
        )
    self.Commit = channel.unary_unary(
        '/sandglass.BrokerService/Commit',
        request_serializer=sandglass__pb2.OffsetChangeRequest.SerializeToString,
        response_deserializer=sandglass__pb2.OffsetChangeReply.FromString,
        )


class BrokerServiceServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def CreateTopic(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetTopic(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Produce(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ProduceMessagesStream(self, request_iterator, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def FetchFrom(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def FetchRange(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ConsumeFromGroup(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Acknowledge(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def AcknowledgeMessages(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Commit(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_BrokerServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'CreateTopic': grpc.unary_unary_rpc_method_handler(
          servicer.CreateTopic,
          request_deserializer=sandglass__pb2.CreateTopicParams.FromString,
          response_serializer=sandglass__pb2.TopicReply.SerializeToString,
      ),
      'GetTopic': grpc.unary_unary_rpc_method_handler(
          servicer.GetTopic,
          request_deserializer=sandglass__pb2.GetTopicParams.FromString,
          response_serializer=sandglass__pb2.GetTopicReply.SerializeToString,
      ),
      'Produce': grpc.unary_unary_rpc_method_handler(
          servicer.Produce,
          request_deserializer=sandglass__pb2.ProduceMessageRequest.FromString,
          response_serializer=sandglass__pb2.ProduceResponse.SerializeToString,
      ),
      'ProduceMessagesStream': grpc.stream_unary_rpc_method_handler(
          servicer.ProduceMessagesStream,
          request_deserializer=sandglass__pb2.Message.FromString,
          response_serializer=sandglass__pb2.StoreLocallyReply.SerializeToString,
      ),
      'FetchFrom': grpc.unary_stream_rpc_method_handler(
          servicer.FetchFrom,
          request_deserializer=sandglass__pb2.FetchFromRequest.FromString,
          response_serializer=sandglass__pb2.Message.SerializeToString,
      ),
      'FetchRange': grpc.unary_stream_rpc_method_handler(
          servicer.FetchRange,
          request_deserializer=sandglass__pb2.FetchRangeRequest.FromString,
          response_serializer=sandglass__pb2.Message.SerializeToString,
      ),
      'ConsumeFromGroup': grpc.unary_stream_rpc_method_handler(
          servicer.ConsumeFromGroup,
          request_deserializer=sandglass__pb2.ConsumeFromGroupRequest.FromString,
          response_serializer=sandglass__pb2.Message.SerializeToString,
      ),
      'Acknowledge': grpc.unary_unary_rpc_method_handler(
          servicer.Acknowledge,
          request_deserializer=sandglass__pb2.OffsetChangeRequest.FromString,
          response_serializer=sandglass__pb2.OffsetChangeReply.SerializeToString,
      ),
      'AcknowledgeMessages': grpc.unary_unary_rpc_method_handler(
          servicer.AcknowledgeMessages,
          request_deserializer=sandglass__pb2.MultiOffsetChangeRequest.FromString,
          response_serializer=sandglass__pb2.OffsetChangeReply.SerializeToString,
      ),
      'Commit': grpc.unary_unary_rpc_method_handler(
          servicer.Commit,
          request_deserializer=sandglass__pb2.OffsetChangeRequest.FromString,
          response_serializer=sandglass__pb2.OffsetChangeReply.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'sandglass.BrokerService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))


class InternalServiceStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.GetByKey = channel.unary_unary(
        '/sandglass.InternalService/GetByKey',
        request_serializer=sandglass__pb2.GetRequest.SerializeToString,
        response_deserializer=sandglass__pb2.Message.FromString,
        )
    self.HasKey = channel.unary_unary(
        '/sandglass.InternalService/HasKey',
        request_serializer=sandglass__pb2.GetRequest.SerializeToString,
        response_deserializer=sandglass__pb2.HasResponse.FromString,
        )
    self.FetchFromSync = channel.unary_stream(
        '/sandglass.InternalService/FetchFromSync',
        request_serializer=sandglass__pb2.FetchFromSyncRequest.SerializeToString,
        response_deserializer=sandglass__pb2.Message.FromString,
        )
    self.LastOffset = channel.unary_unary(
        '/sandglass.InternalService/LastOffset',
        request_serializer=sandglass__pb2.LastOffsetRequest.SerializeToString,
        response_deserializer=sandglass__pb2.LastOffsetReply.FromString,
        )
    self.MarkConsumed = channel.unary_unary(
        '/sandglass.InternalService/MarkConsumed',
        request_serializer=sandglass__pb2.OffsetChangeRequest.SerializeToString,
        response_deserializer=sandglass__pb2.OffsetChangeReply.FromString,
        )
    self.GetMarkStateMessage = channel.unary_unary(
        '/sandglass.InternalService/GetMarkStateMessage',
        request_serializer=sandglass__pb2.OffsetChangeRequest.SerializeToString,
        response_deserializer=sandglass__pb2.Message.FromString,
        )


class InternalServiceServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def GetByKey(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def HasKey(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def FetchFromSync(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def LastOffset(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def MarkConsumed(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetMarkStateMessage(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_InternalServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'GetByKey': grpc.unary_unary_rpc_method_handler(
          servicer.GetByKey,
          request_deserializer=sandglass__pb2.GetRequest.FromString,
          response_serializer=sandglass__pb2.Message.SerializeToString,
      ),
      'HasKey': grpc.unary_unary_rpc_method_handler(
          servicer.HasKey,
          request_deserializer=sandglass__pb2.GetRequest.FromString,
          response_serializer=sandglass__pb2.HasResponse.SerializeToString,
      ),
      'FetchFromSync': grpc.unary_stream_rpc_method_handler(
          servicer.FetchFromSync,
          request_deserializer=sandglass__pb2.FetchFromSyncRequest.FromString,
          response_serializer=sandglass__pb2.Message.SerializeToString,
      ),
      'LastOffset': grpc.unary_unary_rpc_method_handler(
          servicer.LastOffset,
          request_deserializer=sandglass__pb2.LastOffsetRequest.FromString,
          response_serializer=sandglass__pb2.LastOffsetReply.SerializeToString,
      ),
      'MarkConsumed': grpc.unary_unary_rpc_method_handler(
          servicer.MarkConsumed,
          request_deserializer=sandglass__pb2.OffsetChangeRequest.FromString,
          response_serializer=sandglass__pb2.OffsetChangeReply.SerializeToString,
      ),
      'GetMarkStateMessage': grpc.unary_unary_rpc_method_handler(
          servicer.GetMarkStateMessage,
          request_deserializer=sandglass__pb2.OffsetChangeRequest.FromString,
          response_serializer=sandglass__pb2.Message.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'sandglass.InternalService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
