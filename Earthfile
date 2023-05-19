VERSION 0.7
FROM golang:1.20.4-alpine3.18
WORKDIR /grpc

deps:
    ARG protocversion='23.1'
    RUN wget https://github.com/protocolbuffers/protobuf/releases/download/v23.1/protoc-$protocversion-linux-x86_64.zip && \
        unzip -o protoc-$protocversion-linux-x86_64.zip -d /usr/local bin/protoc && \
        unzip -o protoc-$protocversion-linux-x86_64.zip -d /usr/local include/* && \
        rm -rf protoc-$protocversion-linux-x86_64.zip && \
        go install google.golang.org/protobuf/cmd/protoc-gen-go@latest && \
        go install github.com/google/gnostic@latest && \
        apk add git yq && \
        mkdir -p google/api && \
        wget https://raw.githubusercontent.com/googleapis/googleapis/master/google/api/http.proto -O google/api/http.proto && \
        wget https://raw.githubusercontent.com/googleapis/googleapis/master/google/api/annotations.proto -O google/api/annotations.proto
    SAVE ARTIFACT bin/protoc bin/protoc

proto:
    FROM +deps
    COPY openapi.yaml .
    RUN yq 'explode(.)' openapi.yaml > openai.yaml && \
        git clone https://github.com/TylerGillson/gnostic-grpc -b tyler/fix-repeated-props && \
        (cd gnostic-grpc && /bin/sh plugin-creation.sh) && \
        gnostic --grpc-out=. openai.yaml
    SAVE ARTIFACT openai.proto AS LOCAL openai.proto

go-gen:
    FROM +deps
    COPY +proto/openai.proto .
    RUN protoc --go_out=. --go_opt=Mopenai.proto=openai/openai-openapi/proto openai.proto
    SAVE ARTIFACT openai AS LOCAL gen/golang/openai
