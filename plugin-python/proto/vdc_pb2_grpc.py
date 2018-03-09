# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from proto import vdc_pb2 as proto_dot_vdc__pb2


class VdcStub(object):
  """message StorageProfile{
  string name = 1;
  bool is_enabled = 2;
  string units = 3;
  int32 limit = 4;
  bool default = 5;
  }

  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.Create = channel.unary_unary(
        '/proto.Vdc/Create',
        request_serializer=proto_dot_vdc__pb2.CreateVdcInfo.SerializeToString,
        response_deserializer=proto_dot_vdc__pb2.CreateVdcResult.FromString,
        )
    self.Delete = channel.unary_unary(
        '/proto.Vdc/Delete',
        request_serializer=proto_dot_vdc__pb2.DeleteVdcInfo.SerializeToString,
        response_deserializer=proto_dot_vdc__pb2.DeleteVdcResult.FromString,
        )
    self.Read = channel.unary_unary(
        '/proto.Vdc/Read',
        request_serializer=proto_dot_vdc__pb2.ReadVdcInfo.SerializeToString,
        response_deserializer=proto_dot_vdc__pb2.ReadVdcResult.FromString,
        )
    self.Update = channel.unary_unary(
        '/proto.Vdc/Update',
        request_serializer=proto_dot_vdc__pb2.UpdateVdcInfo.SerializeToString,
        response_deserializer=proto_dot_vdc__pb2.UpdateVdcResult.FromString,
        )


class VdcServicer(object):
  """message StorageProfile{
  string name = 1;
  bool is_enabled = 2;
  string units = 3;
  int32 limit = 4;
  bool default = 5;
  }

  """

  def Create(self, request, context):
    """create a Vdc
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Delete(self, request, context):
    """delete a Vdc
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Read(self, request, context):
    """Read Vdc
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Update(self, request, context):
    """Update Vdc
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_VdcServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'Create': grpc.unary_unary_rpc_method_handler(
          servicer.Create,
          request_deserializer=proto_dot_vdc__pb2.CreateVdcInfo.FromString,
          response_serializer=proto_dot_vdc__pb2.CreateVdcResult.SerializeToString,
      ),
      'Delete': grpc.unary_unary_rpc_method_handler(
          servicer.Delete,
          request_deserializer=proto_dot_vdc__pb2.DeleteVdcInfo.FromString,
          response_serializer=proto_dot_vdc__pb2.DeleteVdcResult.SerializeToString,
      ),
      'Read': grpc.unary_unary_rpc_method_handler(
          servicer.Read,
          request_deserializer=proto_dot_vdc__pb2.ReadVdcInfo.FromString,
          response_serializer=proto_dot_vdc__pb2.ReadVdcResult.SerializeToString,
      ),
      'Update': grpc.unary_unary_rpc_method_handler(
          servicer.Update,
          request_deserializer=proto_dot_vdc__pb2.UpdateVdcInfo.FromString,
          response_serializer=proto_dot_vdc__pb2.UpdateVdcResult.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'proto.Vdc', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))