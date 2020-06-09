KERNEL_NAME := hello-kernel

SUBMIT_DIR   := /mnt/cgsubmit
TESTDATA_DIR := /mnt/cgtestdata

all: run

build: 
	docker image rm -f $(KERNEL_NAME)
	docker image build -t $(KERNEL_NAME) .

run: build
	docker run --rm --volume $(CURDIR)/submit:$(SUBMIT_DIR) $(KERNEL_NAME)

img: build
	docker save $(KERNEL_NAME) | gzip -c > $(KERNEL_NAME).tar.gz
