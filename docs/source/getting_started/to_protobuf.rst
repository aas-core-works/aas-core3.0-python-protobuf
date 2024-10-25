******************
To Protocol Buffer
******************

This section explains how to convert AAS V3.0 (Asset Administration Shells) objects into their Protocol Buffer representations.

The conversion lives in :py:mod:`aas_core3_protobuf.pbization` module.

Concrete Classes without Descendants
====================================

The concrete classes without descendants (*i.e.* subtypes) can be directly translated into the corresponding Protocol Buffer structures using a corresponding ``xxx_to_pb``.
For example:

.. doctest::

	import aas_core3.types as aas_types
	import aas_core3_protobuf.types_pb2 as aas_types_pb
	import aas_core3_protobuf.pbization as aas_pbization

	# Initialize the instance
	administrative_information = (
		aas_types.AdministrativeInformation(
			version="19",
			revision="84"
		)
	)

	# Convert it to a Protocol Buffer
	administrative_information_pb = aas_types_pb.AdministrativeInformation()
	aas_pbization.administrative_information_to_pb(
		that=administrative_information,
		target=administrative_information_pb
	)

	# Do something with the Procol Buffer,
	# *e.g.*, serialize it.

	data = administrative_information_pb.SerializeToString()

	print(repr(data))

Expected output:

.. testoutput::

	b'\x12\x0219\x1a\x0284'


We also provide a general :py:func:`aas_core3_protobuf.pbization.to_pb` function which will automatically dispatch to the conversion function based on the runtime type.
The previous example then becomes:

.. doctest::

	import aas_core3.types as aas_types

	import aas_core3_protobuf.pbization as aas_pbization

	# Initialize the instance
	administrative_information = (
		aas_types.AdministrativeInformation(
			version="19",
			revision="84"
		)
	)

	# Convert it to a Protocol Buffer
	message = aas_pbization.to_pb(
		that=administrative_information
	)

	# Do something with the Protocol Buffer,
	# *e.g.*, serialize it.

	data = message.SerializeToString()

	print(repr(data))

Expected output, equal to the previous one:

.. testoutput::

	b'\x12\x0219\x1a\x0284'

Polymorphism
============
Many classes in the AAS meta-model rely on multiple inheritance.
However, the Protocol Buffer does not support inheritance (neither single nor multiple inheritance).
There is but a work around.

For each class with descendants, there is a "choice" Protocol Buffer defined with a single one-of field, distinguishing between the runtime concrete instance nested in the message.

When you convert an instance as an instance of an abstract class, you have to signal that explicitly with ``xxx_to_pb_choice``.
For example, imagine we need to pass over a Protocol Buffer representing a ``SubmodelElement``.
We need to convert a concrete submodel element, say, ``Property``, to this "choice" Protocol Buffer:

.. doctest::

	import aas_core3.types as aas_types
	import aas_core3_protobuf.types_pb2 as aas_types_pb
	import aas_core3_protobuf.pbization as aas_pbization

	# Initialize the instance
	prop = (
		aas_types.Property(
			value_type=aas_types.DataTypeDefXSD.INT,
			value="1984"
		)
	)

	# Convert it to a Protocol Buffer;
	# note that we convert it as a SubmodelElement,
	# and not a Property!

	submodel_element_pb = aas_types_pb.SubmodelElement_choice()
	aas_pbization.submodel_element_to_pb_choice(
		that=prop,
		target=submodel_element_pb
	)

	# Do something with the Protocol Buffer,
	# *e.g.*, serialize it.

	data = submodel_element_pb.SerializeToString()

	print(repr(data))

.. testoutput::

	b'R\x08P\x11Z\x041984'

However, :py:func:`aas_core3_protobuf.pbization.to_pb` can not know which Protocol Buffer you want to use (the concrete one for ``Property`` or the "choice" one for the ``SubmodelElement``).
By design, it will always output the concrete Protocol Buffer:

.. doctest::

	import aas_core3.types as aas_types
	import aas_core3_protobuf.pbization as aas_pbization

	# Initialize the instance
	prop = (
		aas_types.Property(
			value_type=aas_types.DataTypeDefXSD.INT,
			value="1984"
		)
	)

	message = aas_pbization.to_pb(
		that=prop
	)

	# Note the runtime type of this message
	print(type(message))

	# Do something with the Protocol Buffer,
	# *e.g.*, serialize it.

	data = message.SerializeToString()

	# The serialization will obviously differ from the previous
	# example.
	print(repr(data))

.. testoutput::

	<class 'types_pb2.Property'>
	b'P\x11Z\x041984'

You have to be particularly careful in case of a concrete class with descendants.
The instance can analogously be converted either to a Protocol Buffer corresponding to the class or to a "choice" Protocol Buffer.
As in the previous case, :py:func:`aas_core3_protobuf.pbization.to_pb` will always convert to the concrete class.

If you need a "choice" class, call the corresponding ``xxx_to_pb_choice`` function.

Empty and ``None`` Lists
========================

Protocol Buffers do not distinguish between empty (``[]``) and null lists (``None``).
This is problematic, as the AAS meta-model does distinguish between these two cases.

While there is nothing you can do about it, be careful when you have conversions such as JSON — Protocol Buffer — JSON, since this conversion is inherently lossy.
