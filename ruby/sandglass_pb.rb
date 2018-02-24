# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: sandglass.proto

require 'google/protobuf'

require 'google/api/annotations_pb'
require 'google/protobuf/timestamp_pb'
require 'google/protobuf/duration_pb'
Google::Protobuf::DescriptorPool.generated_pool.build do
  add_message "sandglass.Message" do
    optional :index, :uint64, 10
    optional :offset, :bytes, 11
    optional :producedAt, :message, 12, "google.protobuf.Timestamp"
    optional :consumeIn, :message, 13, "google.protobuf.Duration"
    optional :key, :bytes, 20
    optional :clusteringKey, :bytes, 21
    optional :value, :bytes, 30
  end
  add_message "sandglass.ProduceMessageRequest" do
    optional :topic, :string, 1
    optional :partition, :string, 2
    repeated :messages, :message, 3, "sandglass.Message"
  end
  add_message "sandglass.ProduceResponse" do
    repeated :offsets, :bytes, 1
  end
  add_message "sandglass.TopicConfig" do
    optional :name, :string, 1
    optional :kind, :enum, 2, "sandglass.TopicKind"
    optional :replicationFactor, :int32, 3
    optional :numPartitions, :int32, 4
    optional :storageDriver, :enum, 5, "sandglass.StorageDriver"
  end
  add_message "sandglass.GetTopicParams" do
    optional :name, :string, 1
  end
  add_message "sandglass.GetTopicReply" do
    optional :name, :string, 1
    repeated :partitions, :string, 2
  end
  add_message "sandglass.TopicReply" do
    optional :success, :bool, 1
  end
  add_message "sandglass.StoreLocallyReply" do
    optional :success, :bool, 1
  end
  add_message "sandglass.FetchFromRequest" do
    optional :topic, :string, 1
    optional :partition, :string, 2
    optional :from, :bytes, 3
  end
  add_message "sandglass.FetchRangeRequest" do
    optional :topic, :string, 1
    optional :partition, :string, 2
    optional :from, :bytes, 3
    optional :to, :bytes, 4
  end
  add_message "sandglass.GetRequest" do
    optional :topic, :string, 1
    optional :partition, :string, 2
    optional :key, :bytes, 3
    optional :clusteringKey, :bytes, 4
  end
  add_message "sandglass.ConsumeFromGroupRequest" do
    optional :topic, :string, 1
    optional :partition, :string, 2
    optional :consumerGroupName, :string, 3
    optional :consumerName, :string, 4
  end
  add_message "sandglass.MarkRequest" do
    optional :topic, :string, 1
    optional :partition, :string, 2
    optional :consumerGroup, :string, 3
    optional :consumerName, :string, 4
    repeated :offsets, :bytes, 5
    optional :state, :message, 6, "sandglass.MarkState"
  end
  add_message "sandglass.MarkResponse" do
    optional :success, :bool, 1
  end
  add_message "sandglass.GetMarkRequest" do
    optional :topic, :string, 1
    optional :partition, :string, 2
    optional :consumerGroup, :string, 3
    optional :consumerName, :string, 4
    optional :offset, :bytes, 5
  end
  add_message "sandglass.LastOffsetReply" do
    optional :offset, :bytes, 1
  end
  add_message "sandglass.LastOffsetRequest" do
    optional :topic, :string, 1
    optional :partition, :string, 2
    optional :consumerGroup, :string, 3
    optional :consumerName, :string, 4
    optional :kind, :enum, 5, "sandglass.MarkKind"
  end
  add_message "sandglass.FetchFromSyncRequest" do
    optional :topic, :string, 1
    optional :partition, :string, 2
    optional :from, :bytes, 3
  end
  add_message "sandglass.HasResponse" do
    optional :exists, :bool, 1
  end
  add_message "sandglass.MarkState" do
    optional :kind, :enum, 1, "sandglass.MarkKind"
    optional :deliveryCount, :int32, 2
  end
  add_message "sandglass.LastWALIndexRequest" do
  end
  add_message "sandglass.LastWALIndexReply" do
    optional :index, :uint64, 1
  end
  add_message "sandglass.EndOfLogRequest" do
    optional :topic, :string, 1
    optional :partition, :string, 2
  end
  add_message "sandglass.EndOfLogReply" do
    optional :index, :uint64, 1
  end
  add_message "sandglass.MergeState" do
    repeated :messages, :message, 1, "sandglass.Message"
  end
  add_message "sandglass.MergeOperation" do
    optional :operation, :enum, 1, "sandglass.MergeOperation.Operation"
    repeated :messages, :message, 2, "sandglass.Message"
    optional :N, :int32, 3
  end
  add_enum "sandglass.MergeOperation.Operation" do
    value :APPEND, 0
    value :CUT, 1
  end
  add_enum "sandglass.TopicKind" do
    value :TimerKind, 0
    value :KVKind, 1
  end
  add_enum "sandglass.StorageDriver" do
    value :RocksDB, 0
    value :Badger, 1
  end
  add_enum "sandglass.MarkKind" do
    value :Unknown, 0
    value :Consumed, 10
    value :NotAcknowledged, 20
    value :Acknowledged, 30
    value :Commited, 40
  end
end

module Sandglass
  Message = Google::Protobuf::DescriptorPool.generated_pool.lookup("sandglass.Message").msgclass
  ProduceMessageRequest = Google::Protobuf::DescriptorPool.generated_pool.lookup("sandglass.ProduceMessageRequest").msgclass
  ProduceResponse = Google::Protobuf::DescriptorPool.generated_pool.lookup("sandglass.ProduceResponse").msgclass
  TopicConfig = Google::Protobuf::DescriptorPool.generated_pool.lookup("sandglass.TopicConfig").msgclass
  GetTopicParams = Google::Protobuf::DescriptorPool.generated_pool.lookup("sandglass.GetTopicParams").msgclass
  GetTopicReply = Google::Protobuf::DescriptorPool.generated_pool.lookup("sandglass.GetTopicReply").msgclass
  TopicReply = Google::Protobuf::DescriptorPool.generated_pool.lookup("sandglass.TopicReply").msgclass
  StoreLocallyReply = Google::Protobuf::DescriptorPool.generated_pool.lookup("sandglass.StoreLocallyReply").msgclass
  FetchFromRequest = Google::Protobuf::DescriptorPool.generated_pool.lookup("sandglass.FetchFromRequest").msgclass
  FetchRangeRequest = Google::Protobuf::DescriptorPool.generated_pool.lookup("sandglass.FetchRangeRequest").msgclass
  GetRequest = Google::Protobuf::DescriptorPool.generated_pool.lookup("sandglass.GetRequest").msgclass
  ConsumeFromGroupRequest = Google::Protobuf::DescriptorPool.generated_pool.lookup("sandglass.ConsumeFromGroupRequest").msgclass
  MarkRequest = Google::Protobuf::DescriptorPool.generated_pool.lookup("sandglass.MarkRequest").msgclass
  MarkResponse = Google::Protobuf::DescriptorPool.generated_pool.lookup("sandglass.MarkResponse").msgclass
  GetMarkRequest = Google::Protobuf::DescriptorPool.generated_pool.lookup("sandglass.GetMarkRequest").msgclass
  LastOffsetReply = Google::Protobuf::DescriptorPool.generated_pool.lookup("sandglass.LastOffsetReply").msgclass
  LastOffsetRequest = Google::Protobuf::DescriptorPool.generated_pool.lookup("sandglass.LastOffsetRequest").msgclass
  FetchFromSyncRequest = Google::Protobuf::DescriptorPool.generated_pool.lookup("sandglass.FetchFromSyncRequest").msgclass
  HasResponse = Google::Protobuf::DescriptorPool.generated_pool.lookup("sandglass.HasResponse").msgclass
  MarkState = Google::Protobuf::DescriptorPool.generated_pool.lookup("sandglass.MarkState").msgclass
  LastWALIndexRequest = Google::Protobuf::DescriptorPool.generated_pool.lookup("sandglass.LastWALIndexRequest").msgclass
  LastWALIndexReply = Google::Protobuf::DescriptorPool.generated_pool.lookup("sandglass.LastWALIndexReply").msgclass
  EndOfLogRequest = Google::Protobuf::DescriptorPool.generated_pool.lookup("sandglass.EndOfLogRequest").msgclass
  EndOfLogReply = Google::Protobuf::DescriptorPool.generated_pool.lookup("sandglass.EndOfLogReply").msgclass
  MergeState = Google::Protobuf::DescriptorPool.generated_pool.lookup("sandglass.MergeState").msgclass
  MergeOperation = Google::Protobuf::DescriptorPool.generated_pool.lookup("sandglass.MergeOperation").msgclass
  MergeOperation::Operation = Google::Protobuf::DescriptorPool.generated_pool.lookup("sandglass.MergeOperation.Operation").enummodule
  TopicKind = Google::Protobuf::DescriptorPool.generated_pool.lookup("sandglass.TopicKind").enummodule
  StorageDriver = Google::Protobuf::DescriptorPool.generated_pool.lookup("sandglass.StorageDriver").enummodule
  MarkKind = Google::Protobuf::DescriptorPool.generated_pool.lookup("sandglass.MarkKind").enummodule
end
