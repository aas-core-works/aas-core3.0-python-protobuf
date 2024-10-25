********************
From Protocol Buffer
********************
In this section, we will dive into transforming AAS V3.0 (Asset Administration Shell) objects from their Protocol Buffer representation.

The conversion process is handled within the :py:mod:`aas_core3_protobuf.pbization` module.

Concrete Classes without Descendants
====================================

Classes without descendants (*i.e.* subtypes) can be directly converted from their matching Protocol Buffer structures using the respective ``xxx_from_pb`` function.
For example:

.. doctest::

	import json

	import aas_core3.types as aas_types
	import aas_core3.jsonization as aas_jsonization

	import aas_core3_protobuf.pbization as aas_pbization
	import aas_core3_protobuf.types_pb2 as aas_types_pb

	# Initialize the Protocol Buffer
	administrative_information_pb = (
		aas_types_pb.AdministrativeInformation(
			version="19",
			revision="84"
		)
	)

	administrative_information = (
		aas_pbization.administrative_information_from_pb(
			administrative_information_pb
		)
	)

	assert isinstance(
		administrative_information,
		aas_types.AdministrativeInformation
	)

	print(
		json.dumps(
			aas_jsonization.to_jsonable(
				administrative_information
			)
		)
	)

Expected output:

.. testoutput::

	{"version": "19", "revision": "84"}

We also provide a general function for conversion of model instances back from their Protocol Buffer representation, :py:func:`aas_core3_protobuf.pbization.from_pb`.
This function checks the runtime type of the protocol buffer, and forwards the conversion to the respective ``xxx_from_pb`` or ``xxx_from_pb_choice``.

It is important to note that the serialization of Protocol Buffers does not carry any runtime type information, so the type must be known before serialization.
In other words, there is no general ``DeserializeFromString`` for Protocol Buffers.

Here is an example that shows the whole chain, from bytes to a model instance:

.. doctest::

	import aas_core3_protobuf.pbization as aas_pbization
	import aas_core3_protobuf.types_pb2 as aas_types_pb

	data = b'\x12\x0219\x1a\x0284'

	# You have to know what you de-serialize.
	protobuf = (
		aas_types_pb.AdministrativeInformation.FromString(
			data
		)
	)

	# ``from_pb`` will dynamically decide what conversion
	# function to use.
	instance = (
		aas_pbization.from_pb(
			protobuf
		)
	)

	print(instance.__class__.__name__)

Expected output:

.. testoutput::

	AdministrativeInformation

There are two relevant distinctions between a specific ``xxx_from_pb`` and :py:func:`aas_core3_protobuf.pbization.from_pb` even though their runtime behavior is similar.
Namely, their type annotations and their preconditions differ.

A specific ``xxx_from_pb`` expects the protocol buffer corresponding to the concrete class.
If you pass in a protocol buffer for a different class, the conversion will fail with an exception.
Analogously, the return type is specifically annotated with the class ``Xxx``.
For example, see the signature of the specific :py:func:`aas_core3_protobuf.pbization.administrative_information_from_pb`.

The behavior of :py:func:`aas_core3_protobuf.pbization.from_pb` will adapt dynamically to the runtime type of the given protocol buffer.
As long as the protocol buffer comes from :py:mod:`aas_core3_protobuf.types_pb2`, it will be converted to a model instance.
However, as we can not know the outcome before the execution, the return type of the :py:func:`aas_core3_protobuf.pbization.from_pb` can only be annotated with the most general class, :py:class:`aas_core3.types.Class`.

Polymorphism
============
The polymorphism in Protocol Buffers is implemented through so called "choice" classes (a.k.a. "union" classes or types).
Such "choice" classes contain only a single one-of field which nests the concrete protocol buffer.

To convert from such a "choice" class, you can either use the specific conversion function ``xxx_from_pb_choice`` or the general one, :py:func:`aas_core3_protobuf.pbization.from_pb`.

Please see the previous section for the difference between the two.

Empty and ``None`` Lists
========================
As Protocol Buffers ignore the difference between ``None`` lists and empty lists (``[]``), both values will be stored the same in a message.
When the message is de-serialized from the bytes, you can not distinguish what was the original value.

In contrast, AAS SDK does distinguish between the two.
Many model instances can not be exactly represented in Protocol Buffers as a consequence.
By design, we decided to work around that issue with the following convention:

* If a property of a class is optional list, we convert the empty Protocol Buffer field to a ``None``.
* If a property is a required list, we convert the field to an empty list (``[]``).
