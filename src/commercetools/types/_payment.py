# DO NOT EDIT! This file is automatically generated

import datetime
import enum
import typing

import attr

from commercetools.types._base import PagedQueryResponse, Update, UpdateAction
from commercetools.types._common import Reference, ReferenceTypeId, Resource

if typing.TYPE_CHECKING:
    from ._common import LocalizedString, Money, TypedMoney
    from ._customer import CustomerReference
    from ._state import StateReference
    from ._type import CustomFields, CustomFieldsDraft, FieldContainer, TypeReference
__all__ = [
    "Payment",
    "PaymentAddInterfaceInteractionAction",
    "PaymentAddTransactionAction",
    "PaymentChangeAmountPlannedAction",
    "PaymentChangeTransactionInteractionIdAction",
    "PaymentChangeTransactionStateAction",
    "PaymentChangeTransactionTimestampAction",
    "PaymentDraft",
    "PaymentMethodInfo",
    "PaymentPagedQueryResponse",
    "PaymentReference",
    "PaymentSetAmountPaidAction",
    "PaymentSetAmountRefundedAction",
    "PaymentSetAnonymousIdAction",
    "PaymentSetAuthorizationAction",
    "PaymentSetCustomFieldAction",
    "PaymentSetCustomTypeAction",
    "PaymentSetCustomerAction",
    "PaymentSetExternalIdAction",
    "PaymentSetInterfaceIdAction",
    "PaymentSetKeyAction",
    "PaymentSetMethodInfoInterfaceAction",
    "PaymentSetMethodInfoMethodAction",
    "PaymentSetMethodInfoNameAction",
    "PaymentSetStatusInterfaceCodeAction",
    "PaymentSetStatusInterfaceTextAction",
    "PaymentStatus",
    "PaymentTransitionStateAction",
    "PaymentUpdate",
    "PaymentUpdateAction",
    "Transaction",
    "TransactionDraft",
    "TransactionState",
    "TransactionType",
]


@attr.s(auto_attribs=True, init=False, repr=False)
class PaymentDraft:
    "Corresponding marshmallow schema is :class:`commercetools.schemas.PaymentDraftSchema`."
    #: Optional :class:`commercetools.types.CustomerReference`
    customer: typing.Optional["CustomerReference"]
    #: Optional :class:`str` `(Named` ``anonymousId`` `in Commercetools)`
    anonymous_id: typing.Optional[str]
    #: Optional :class:`str` `(Named` ``externalId`` `in Commercetools)`
    external_id: typing.Optional[str]
    #: Optional :class:`str` `(Named` ``interfaceId`` `in Commercetools)`
    interface_id: typing.Optional[str]
    #: :class:`commercetools.types.Money` `(Named` ``amountPlanned`` `in Commercetools)`
    amount_planned: typing.Optional["Money"]
    #: Optional :class:`commercetools.types.Money` `(Named` ``amountAuthorized`` `in Commercetools)`
    amount_authorized: typing.Optional["Money"]
    #: Optional :class:`str` `(Named` ``authorizedUntil`` `in Commercetools)`
    authorized_until: typing.Optional[str]
    #: Optional :class:`commercetools.types.Money` `(Named` ``amountPaid`` `in Commercetools)`
    amount_paid: typing.Optional["Money"]
    #: Optional :class:`commercetools.types.Money` `(Named` ``amountRefunded`` `in Commercetools)`
    amount_refunded: typing.Optional["Money"]
    #: Optional :class:`commercetools.types.PaymentMethodInfo` `(Named` ``paymentMethodInfo`` `in Commercetools)`
    payment_method_info: typing.Optional["PaymentMethodInfo"]
    #: Optional :class:`commercetools.types.PaymentStatus` `(Named` ``paymentStatus`` `in Commercetools)`
    payment_status: typing.Optional["PaymentStatus"]
    #: Optional list of :class:`commercetools.types.TransactionDraft`
    transactions: typing.Optional[typing.List["TransactionDraft"]]
    #: Optional list of :class:`commercetools.types.CustomFieldsDraft` `(Named` ``interfaceInteractions`` `in Commercetools)`
    interface_interactions: typing.Optional[typing.List["CustomFieldsDraft"]]
    #: Optional :class:`commercetools.types.CustomFieldsDraft`
    custom: typing.Optional["CustomFieldsDraft"]
    #: Optional :class:`str`
    key: typing.Optional[str]

    def __init__(
        self,
        *,
        customer: typing.Optional["CustomerReference"] = None,
        anonymous_id: typing.Optional[str] = None,
        external_id: typing.Optional[str] = None,
        interface_id: typing.Optional[str] = None,
        amount_planned: typing.Optional["Money"] = None,
        amount_authorized: typing.Optional["Money"] = None,
        authorized_until: typing.Optional[str] = None,
        amount_paid: typing.Optional["Money"] = None,
        amount_refunded: typing.Optional["Money"] = None,
        payment_method_info: typing.Optional["PaymentMethodInfo"] = None,
        payment_status: typing.Optional["PaymentStatus"] = None,
        transactions: typing.Optional[typing.List["TransactionDraft"]] = None,
        interface_interactions: typing.Optional[
            typing.List["CustomFieldsDraft"]
        ] = None,
        custom: typing.Optional["CustomFieldsDraft"] = None,
        key: typing.Optional[str] = None
    ) -> None:
        self.customer = customer
        self.anonymous_id = anonymous_id
        self.external_id = external_id
        self.interface_id = interface_id
        self.amount_planned = amount_planned
        self.amount_authorized = amount_authorized
        self.authorized_until = authorized_until
        self.amount_paid = amount_paid
        self.amount_refunded = amount_refunded
        self.payment_method_info = payment_method_info
        self.payment_status = payment_status
        self.transactions = transactions
        self.interface_interactions = interface_interactions
        self.custom = custom
        self.key = key

    def __repr__(self) -> str:
        return (
            "PaymentDraft(customer=%r, anonymous_id=%r, external_id=%r, interface_id=%r, amount_planned=%r, amount_authorized=%r, authorized_until=%r, amount_paid=%r, amount_refunded=%r, payment_method_info=%r, payment_status=%r, transactions=%r, interface_interactions=%r, custom=%r, key=%r)"
            % (
                self.customer,
                self.anonymous_id,
                self.external_id,
                self.interface_id,
                self.amount_planned,
                self.amount_authorized,
                self.authorized_until,
                self.amount_paid,
                self.amount_refunded,
                self.payment_method_info,
                self.payment_status,
                self.transactions,
                self.interface_interactions,
                self.custom,
                self.key,
            )
        )


@attr.s(auto_attribs=True, init=False, repr=False)
class PaymentMethodInfo:
    "Corresponding marshmallow schema is :class:`commercetools.schemas.PaymentMethodInfoSchema`."
    #: Optional :class:`str` `(Named` ``paymentInterface`` `in Commercetools)`
    payment_interface: typing.Optional[str]
    #: Optional :class:`str`
    method: typing.Optional[str]
    #: Optional :class:`commercetools.types.LocalizedString`
    name: typing.Optional["LocalizedString"]

    def __init__(
        self,
        *,
        payment_interface: typing.Optional[str] = None,
        method: typing.Optional[str] = None,
        name: typing.Optional["LocalizedString"] = None
    ) -> None:
        self.payment_interface = payment_interface
        self.method = method
        self.name = name

    def __repr__(self) -> str:
        return "PaymentMethodInfo(payment_interface=%r, method=%r, name=%r)" % (
            self.payment_interface,
            self.method,
            self.name,
        )


@attr.s(auto_attribs=True, init=False, repr=False)
class PaymentStatus:
    "Corresponding marshmallow schema is :class:`commercetools.schemas.PaymentStatusSchema`."
    #: Optional :class:`str` `(Named` ``interfaceCode`` `in Commercetools)`
    interface_code: typing.Optional[str]
    #: Optional :class:`str` `(Named` ``interfaceText`` `in Commercetools)`
    interface_text: typing.Optional[str]
    #: Optional :class:`commercetools.types.StateReference`
    state: typing.Optional["StateReference"]

    def __init__(
        self,
        *,
        interface_code: typing.Optional[str] = None,
        interface_text: typing.Optional[str] = None,
        state: typing.Optional["StateReference"] = None
    ) -> None:
        self.interface_code = interface_code
        self.interface_text = interface_text
        self.state = state

    def __repr__(self) -> str:
        return "PaymentStatus(interface_code=%r, interface_text=%r, state=%r)" % (
            self.interface_code,
            self.interface_text,
            self.state,
        )


@attr.s(auto_attribs=True, init=False, repr=False)
class Transaction:
    "Corresponding marshmallow schema is :class:`commercetools.schemas.TransactionSchema`."
    #: :class:`str`
    id: typing.Optional[str]
    #: Optional :class:`datetime.datetime`
    timestamp: typing.Optional[datetime.datetime]
    #: :class:`commercetools.types.TransactionType`
    type: typing.Optional["TransactionType"]
    #: :class:`commercetools.types.TypedMoney`
    amount: typing.Optional["TypedMoney"]
    #: Optional :class:`str` `(Named` ``interactionId`` `in Commercetools)`
    interaction_id: typing.Optional[str]
    #: Optional :class:`commercetools.types.TransactionState`
    state: typing.Optional["TransactionState"]

    def __init__(
        self,
        *,
        id: typing.Optional[str] = None,
        timestamp: typing.Optional[datetime.datetime] = None,
        type: typing.Optional["TransactionType"] = None,
        amount: typing.Optional["TypedMoney"] = None,
        interaction_id: typing.Optional[str] = None,
        state: typing.Optional["TransactionState"] = None
    ) -> None:
        self.id = id
        self.timestamp = timestamp
        self.type = type
        self.amount = amount
        self.interaction_id = interaction_id
        self.state = state

    def __repr__(self) -> str:
        return (
            "Transaction(id=%r, timestamp=%r, type=%r, amount=%r, interaction_id=%r, state=%r)"
            % (
                self.id,
                self.timestamp,
                self.type,
                self.amount,
                self.interaction_id,
                self.state,
            )
        )


@attr.s(auto_attribs=True, init=False, repr=False)
class TransactionDraft:
    "Corresponding marshmallow schema is :class:`commercetools.schemas.TransactionDraftSchema`."
    #: Optional :class:`datetime.datetime`
    timestamp: typing.Optional[datetime.datetime]
    #: :class:`commercetools.types.TransactionType`
    type: typing.Optional["TransactionType"]
    #: :class:`commercetools.types.Money`
    amount: typing.Optional["Money"]
    #: Optional :class:`str` `(Named` ``interactionId`` `in Commercetools)`
    interaction_id: typing.Optional[str]
    #: Optional :class:`commercetools.types.TransactionState`
    state: typing.Optional["TransactionState"]

    def __init__(
        self,
        *,
        timestamp: typing.Optional[datetime.datetime] = None,
        type: typing.Optional["TransactionType"] = None,
        amount: typing.Optional["Money"] = None,
        interaction_id: typing.Optional[str] = None,
        state: typing.Optional["TransactionState"] = None
    ) -> None:
        self.timestamp = timestamp
        self.type = type
        self.amount = amount
        self.interaction_id = interaction_id
        self.state = state

    def __repr__(self) -> str:
        return (
            "TransactionDraft(timestamp=%r, type=%r, amount=%r, interaction_id=%r, state=%r)"
            % (self.timestamp, self.type, self.amount, self.interaction_id, self.state)
        )


@attr.s(auto_attribs=True, init=False, repr=False)
class Payment(Resource):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.PaymentSchema`."
    #: Optional :class:`commercetools.types.CustomerReference`
    customer: typing.Optional["CustomerReference"]
    #: Optional :class:`str` `(Named` ``anonymousId`` `in Commercetools)`
    anonymous_id: typing.Optional[str]
    #: Optional :class:`str` `(Named` ``externalId`` `in Commercetools)`
    external_id: typing.Optional[str]
    #: Optional :class:`str` `(Named` ``interfaceId`` `in Commercetools)`
    interface_id: typing.Optional[str]
    #: :class:`commercetools.types.TypedMoney` `(Named` ``amountPlanned`` `in Commercetools)`
    amount_planned: typing.Optional["TypedMoney"]
    #: Optional :class:`commercetools.types.TypedMoney` `(Named` ``amountAuthorized`` `in Commercetools)`
    amount_authorized: typing.Optional["TypedMoney"]
    #: Optional :class:`str` `(Named` ``authorizedUntil`` `in Commercetools)`
    authorized_until: typing.Optional[str]
    #: Optional :class:`commercetools.types.TypedMoney` `(Named` ``amountPaid`` `in Commercetools)`
    amount_paid: typing.Optional["TypedMoney"]
    #: Optional :class:`commercetools.types.TypedMoney` `(Named` ``amountRefunded`` `in Commercetools)`
    amount_refunded: typing.Optional["TypedMoney"]
    #: :class:`commercetools.types.PaymentMethodInfo` `(Named` ``paymentMethodInfo`` `in Commercetools)`
    payment_method_info: typing.Optional["PaymentMethodInfo"]
    #: :class:`commercetools.types.PaymentStatus` `(Named` ``paymentStatus`` `in Commercetools)`
    payment_status: typing.Optional["PaymentStatus"]
    #: List of :class:`commercetools.types.Transaction`
    transactions: typing.Optional[typing.List["Transaction"]]
    #: List of :class:`commercetools.types.CustomFields` `(Named` ``interfaceInteractions`` `in Commercetools)`
    interface_interactions: typing.Optional[typing.List["CustomFields"]]
    #: Optional :class:`commercetools.types.CustomFields`
    custom: typing.Optional["CustomFields"]
    #: Optional :class:`str`
    key: typing.Optional[str]

    def __init__(
        self,
        *,
        id: typing.Optional[str] = None,
        version: typing.Optional[int] = None,
        created_at: typing.Optional[datetime.datetime] = None,
        last_modified_at: typing.Optional[datetime.datetime] = None,
        customer: typing.Optional["CustomerReference"] = None,
        anonymous_id: typing.Optional[str] = None,
        external_id: typing.Optional[str] = None,
        interface_id: typing.Optional[str] = None,
        amount_planned: typing.Optional["TypedMoney"] = None,
        amount_authorized: typing.Optional["TypedMoney"] = None,
        authorized_until: typing.Optional[str] = None,
        amount_paid: typing.Optional["TypedMoney"] = None,
        amount_refunded: typing.Optional["TypedMoney"] = None,
        payment_method_info: typing.Optional["PaymentMethodInfo"] = None,
        payment_status: typing.Optional["PaymentStatus"] = None,
        transactions: typing.Optional[typing.List["Transaction"]] = None,
        interface_interactions: typing.Optional[typing.List["CustomFields"]] = None,
        custom: typing.Optional["CustomFields"] = None,
        key: typing.Optional[str] = None
    ) -> None:
        self.customer = customer
        self.anonymous_id = anonymous_id
        self.external_id = external_id
        self.interface_id = interface_id
        self.amount_planned = amount_planned
        self.amount_authorized = amount_authorized
        self.authorized_until = authorized_until
        self.amount_paid = amount_paid
        self.amount_refunded = amount_refunded
        self.payment_method_info = payment_method_info
        self.payment_status = payment_status
        self.transactions = transactions
        self.interface_interactions = interface_interactions
        self.custom = custom
        self.key = key
        super().__init__(
            id=id,
            version=version,
            created_at=created_at,
            last_modified_at=last_modified_at,
        )

    def __repr__(self) -> str:
        return (
            "Payment(id=%r, version=%r, created_at=%r, last_modified_at=%r, customer=%r, anonymous_id=%r, external_id=%r, interface_id=%r, amount_planned=%r, amount_authorized=%r, authorized_until=%r, amount_paid=%r, amount_refunded=%r, payment_method_info=%r, payment_status=%r, transactions=%r, interface_interactions=%r, custom=%r, key=%r)"
            % (
                self.id,
                self.version,
                self.created_at,
                self.last_modified_at,
                self.customer,
                self.anonymous_id,
                self.external_id,
                self.interface_id,
                self.amount_planned,
                self.amount_authorized,
                self.authorized_until,
                self.amount_paid,
                self.amount_refunded,
                self.payment_method_info,
                self.payment_status,
                self.transactions,
                self.interface_interactions,
                self.custom,
                self.key,
            )
        )


@attr.s(auto_attribs=True, init=False, repr=False)
class PaymentPagedQueryResponse(PagedQueryResponse):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.PaymentPagedQueryResponseSchema`."
    #: List of :class:`commercetools.types.Payment`
    results: typing.Optional[typing.Sequence["Payment"]]

    def __init__(
        self,
        *,
        count: typing.Optional[int] = None,
        total: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        results: typing.Optional[typing.Sequence["Payment"]] = None
    ) -> None:
        self.results = results
        super().__init__(count=count, total=total, offset=offset, results=results)

    def __repr__(self) -> str:
        return (
            "PaymentPagedQueryResponse(count=%r, total=%r, offset=%r, results=%r)"
            % (self.count, self.total, self.offset, self.results)
        )


@attr.s(auto_attribs=True, init=False, repr=False)
class PaymentReference(Reference):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.PaymentReferenceSchema`."
    #: Optional :class:`commercetools.types.Payment`
    obj: typing.Optional["Payment"]

    def __init__(
        self,
        *,
        type_id: typing.Optional["ReferenceTypeId"] = None,
        id: typing.Optional[str] = None,
        key: typing.Optional[str] = None,
        obj: typing.Optional["Payment"] = None
    ) -> None:
        self.obj = obj
        super().__init__(type_id=ReferenceTypeId.PAYMENT, id=id, key=key)

    def __repr__(self) -> str:
        return "PaymentReference(type_id=%r, id=%r, key=%r, obj=%r)" % (
            self.type_id,
            self.id,
            self.key,
            self.obj,
        )


@attr.s(auto_attribs=True, init=False, repr=False)
class PaymentUpdate(Update):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.PaymentUpdateSchema`."
    #: :class:`list`
    actions: typing.Optional[list]

    def __init__(
        self,
        *,
        version: typing.Optional[int] = None,
        actions: typing.Optional[list] = None
    ) -> None:
        self.actions = actions
        super().__init__(version=version, actions=actions)

    def __repr__(self) -> str:
        return "PaymentUpdate(version=%r, actions=%r)" % (self.version, self.actions)


@attr.s(auto_attribs=True, init=False, repr=False)
class PaymentUpdateAction(UpdateAction):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.PaymentUpdateActionSchema`."

    def __init__(self, *, action: typing.Optional[str] = None) -> None:
        super().__init__(action=action)

    def __repr__(self) -> str:
        return "PaymentUpdateAction(action=%r)" % (self.action,)


class TransactionState(enum.Enum):
    INITIAL = "Initial"
    PENDING = "Pending"
    SUCCESS = "Success"
    FAILURE = "Failure"


class TransactionType(enum.Enum):
    AUTHORIZATION = "Authorization"
    CANCEL_AUTHORIZATION = "CancelAuthorization"
    CHARGE = "Charge"
    REFUND = "Refund"
    CHARGEBACK = "Chargeback"


@attr.s(auto_attribs=True, init=False, repr=False)
class PaymentAddInterfaceInteractionAction(PaymentUpdateAction):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.PaymentAddInterfaceInteractionActionSchema`."
    #: :class:`commercetools.types.TypeReference`
    type: typing.Optional["TypeReference"]
    #: Optional :class:`commercetools.types.FieldContainer`
    fields: typing.Optional["FieldContainer"]

    def __init__(
        self,
        *,
        action: typing.Optional[str] = None,
        type: typing.Optional["TypeReference"] = None,
        fields: typing.Optional["FieldContainer"] = None
    ) -> None:
        self.type = type
        self.fields = fields
        super().__init__(action="addInterfaceInteraction")

    def __repr__(self) -> str:
        return "PaymentAddInterfaceInteractionAction(action=%r, type=%r, fields=%r)" % (
            self.action,
            self.type,
            self.fields,
        )


@attr.s(auto_attribs=True, init=False, repr=False)
class PaymentAddTransactionAction(PaymentUpdateAction):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.PaymentAddTransactionActionSchema`."
    #: :class:`commercetools.types.TransactionDraft`
    transaction: typing.Optional["TransactionDraft"]

    def __init__(
        self,
        *,
        action: typing.Optional[str] = None,
        transaction: typing.Optional["TransactionDraft"] = None
    ) -> None:
        self.transaction = transaction
        super().__init__(action="addTransaction")

    def __repr__(self) -> str:
        return "PaymentAddTransactionAction(action=%r, transaction=%r)" % (
            self.action,
            self.transaction,
        )


@attr.s(auto_attribs=True, init=False, repr=False)
class PaymentChangeAmountPlannedAction(PaymentUpdateAction):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.PaymentChangeAmountPlannedActionSchema`."
    #: :class:`commercetools.types.Money`
    amount: typing.Optional["Money"]

    def __init__(
        self,
        *,
        action: typing.Optional[str] = None,
        amount: typing.Optional["Money"] = None
    ) -> None:
        self.amount = amount
        super().__init__(action="changeAmountPlanned")

    def __repr__(self) -> str:
        return "PaymentChangeAmountPlannedAction(action=%r, amount=%r)" % (
            self.action,
            self.amount,
        )


@attr.s(auto_attribs=True, init=False, repr=False)
class PaymentChangeTransactionInteractionIdAction(PaymentUpdateAction):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.PaymentChangeTransactionInteractionIdActionSchema`."
    #: :class:`str` `(Named` ``transactionId`` `in Commercetools)`
    transaction_id: typing.Optional[str]
    #: :class:`str` `(Named` ``interactionId`` `in Commercetools)`
    interaction_id: typing.Optional[str]

    def __init__(
        self,
        *,
        action: typing.Optional[str] = None,
        transaction_id: typing.Optional[str] = None,
        interaction_id: typing.Optional[str] = None
    ) -> None:
        self.transaction_id = transaction_id
        self.interaction_id = interaction_id
        super().__init__(action="changeTransactionInteractionId")

    def __repr__(self) -> str:
        return (
            "PaymentChangeTransactionInteractionIdAction(action=%r, transaction_id=%r, interaction_id=%r)"
            % (self.action, self.transaction_id, self.interaction_id)
        )


@attr.s(auto_attribs=True, init=False, repr=False)
class PaymentChangeTransactionStateAction(PaymentUpdateAction):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.PaymentChangeTransactionStateActionSchema`."
    #: :class:`str` `(Named` ``transactionId`` `in Commercetools)`
    transaction_id: typing.Optional[str]
    #: :class:`commercetools.types.TransactionState`
    state: typing.Optional["TransactionState"]

    def __init__(
        self,
        *,
        action: typing.Optional[str] = None,
        transaction_id: typing.Optional[str] = None,
        state: typing.Optional["TransactionState"] = None
    ) -> None:
        self.transaction_id = transaction_id
        self.state = state
        super().__init__(action="changeTransactionState")

    def __repr__(self) -> str:
        return (
            "PaymentChangeTransactionStateAction(action=%r, transaction_id=%r, state=%r)"
            % (self.action, self.transaction_id, self.state)
        )


@attr.s(auto_attribs=True, init=False, repr=False)
class PaymentChangeTransactionTimestampAction(PaymentUpdateAction):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.PaymentChangeTransactionTimestampActionSchema`."
    #: :class:`str` `(Named` ``transactionId`` `in Commercetools)`
    transaction_id: typing.Optional[str]
    #: :class:`datetime.datetime`
    timestamp: typing.Optional[datetime.datetime]

    def __init__(
        self,
        *,
        action: typing.Optional[str] = None,
        transaction_id: typing.Optional[str] = None,
        timestamp: typing.Optional[datetime.datetime] = None
    ) -> None:
        self.transaction_id = transaction_id
        self.timestamp = timestamp
        super().__init__(action="changeTransactionTimestamp")

    def __repr__(self) -> str:
        return (
            "PaymentChangeTransactionTimestampAction(action=%r, transaction_id=%r, timestamp=%r)"
            % (self.action, self.transaction_id, self.timestamp)
        )


@attr.s(auto_attribs=True, init=False, repr=False)
class PaymentSetAmountPaidAction(PaymentUpdateAction):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.PaymentSetAmountPaidActionSchema`."
    #: Optional :class:`commercetools.types.Money`
    amount: typing.Optional["Money"]

    def __init__(
        self,
        *,
        action: typing.Optional[str] = None,
        amount: typing.Optional["Money"] = None
    ) -> None:
        self.amount = amount
        super().__init__(action="setAmountPaid")

    def __repr__(self) -> str:
        return "PaymentSetAmountPaidAction(action=%r, amount=%r)" % (
            self.action,
            self.amount,
        )


@attr.s(auto_attribs=True, init=False, repr=False)
class PaymentSetAmountRefundedAction(PaymentUpdateAction):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.PaymentSetAmountRefundedActionSchema`."
    #: Optional :class:`commercetools.types.Money`
    amount: typing.Optional["Money"]

    def __init__(
        self,
        *,
        action: typing.Optional[str] = None,
        amount: typing.Optional["Money"] = None
    ) -> None:
        self.amount = amount
        super().__init__(action="setAmountRefunded")

    def __repr__(self) -> str:
        return "PaymentSetAmountRefundedAction(action=%r, amount=%r)" % (
            self.action,
            self.amount,
        )


@attr.s(auto_attribs=True, init=False, repr=False)
class PaymentSetAnonymousIdAction(PaymentUpdateAction):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.PaymentSetAnonymousIdActionSchema`."
    #: Optional :class:`str` `(Named` ``anonymousId`` `in Commercetools)`
    anonymous_id: typing.Optional[str]

    def __init__(
        self,
        *,
        action: typing.Optional[str] = None,
        anonymous_id: typing.Optional[str] = None
    ) -> None:
        self.anonymous_id = anonymous_id
        super().__init__(action="setAnonymousId")

    def __repr__(self) -> str:
        return "PaymentSetAnonymousIdAction(action=%r, anonymous_id=%r)" % (
            self.action,
            self.anonymous_id,
        )


@attr.s(auto_attribs=True, init=False, repr=False)
class PaymentSetAuthorizationAction(PaymentUpdateAction):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.PaymentSetAuthorizationActionSchema`."
    #: Optional :class:`commercetools.types.Money`
    amount: typing.Optional["Money"]
    #: Optional :class:`datetime.datetime`
    until: typing.Optional[datetime.datetime]

    def __init__(
        self,
        *,
        action: typing.Optional[str] = None,
        amount: typing.Optional["Money"] = None,
        until: typing.Optional[datetime.datetime] = None
    ) -> None:
        self.amount = amount
        self.until = until
        super().__init__(action="setAuthorization")

    def __repr__(self) -> str:
        return "PaymentSetAuthorizationAction(action=%r, amount=%r, until=%r)" % (
            self.action,
            self.amount,
            self.until,
        )


@attr.s(auto_attribs=True, init=False, repr=False)
class PaymentSetCustomFieldAction(PaymentUpdateAction):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.PaymentSetCustomFieldActionSchema`."
    #: :class:`str`
    name: typing.Optional[str]
    #: Optional :class:`typing.Any`
    value: typing.Optional[typing.Any]

    def __init__(
        self,
        *,
        action: typing.Optional[str] = None,
        name: typing.Optional[str] = None,
        value: typing.Optional[typing.Any] = None
    ) -> None:
        self.name = name
        self.value = value
        super().__init__(action="setCustomField")

    def __repr__(self) -> str:
        return "PaymentSetCustomFieldAction(action=%r, name=%r, value=%r)" % (
            self.action,
            self.name,
            self.value,
        )


@attr.s(auto_attribs=True, init=False, repr=False)
class PaymentSetCustomTypeAction(PaymentUpdateAction):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.PaymentSetCustomTypeActionSchema`."
    #: Optional :class:`commercetools.types.TypeReference`
    type: typing.Optional["TypeReference"]
    #: Optional :class:`commercetools.types.FieldContainer`
    fields: typing.Optional["FieldContainer"]

    def __init__(
        self,
        *,
        action: typing.Optional[str] = None,
        type: typing.Optional["TypeReference"] = None,
        fields: typing.Optional["FieldContainer"] = None
    ) -> None:
        self.type = type
        self.fields = fields
        super().__init__(action="setCustomType")

    def __repr__(self) -> str:
        return "PaymentSetCustomTypeAction(action=%r, type=%r, fields=%r)" % (
            self.action,
            self.type,
            self.fields,
        )


@attr.s(auto_attribs=True, init=False, repr=False)
class PaymentSetCustomerAction(PaymentUpdateAction):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.PaymentSetCustomerActionSchema`."
    #: Optional :class:`commercetools.types.CustomerReference`
    customer: typing.Optional["CustomerReference"]

    def __init__(
        self,
        *,
        action: typing.Optional[str] = None,
        customer: typing.Optional["CustomerReference"] = None
    ) -> None:
        self.customer = customer
        super().__init__(action="setCustomer")

    def __repr__(self) -> str:
        return "PaymentSetCustomerAction(action=%r, customer=%r)" % (
            self.action,
            self.customer,
        )


@attr.s(auto_attribs=True, init=False, repr=False)
class PaymentSetExternalIdAction(PaymentUpdateAction):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.PaymentSetExternalIdActionSchema`."
    #: Optional :class:`str` `(Named` ``externalId`` `in Commercetools)`
    external_id: typing.Optional[str]

    def __init__(
        self,
        *,
        action: typing.Optional[str] = None,
        external_id: typing.Optional[str] = None
    ) -> None:
        self.external_id = external_id
        super().__init__(action="setExternalId")

    def __repr__(self) -> str:
        return "PaymentSetExternalIdAction(action=%r, external_id=%r)" % (
            self.action,
            self.external_id,
        )


@attr.s(auto_attribs=True, init=False, repr=False)
class PaymentSetInterfaceIdAction(PaymentUpdateAction):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.PaymentSetInterfaceIdActionSchema`."
    #: :class:`str` `(Named` ``interfaceId`` `in Commercetools)`
    interface_id: typing.Optional[str]

    def __init__(
        self,
        *,
        action: typing.Optional[str] = None,
        interface_id: typing.Optional[str] = None
    ) -> None:
        self.interface_id = interface_id
        super().__init__(action="setInterfaceId")

    def __repr__(self) -> str:
        return "PaymentSetInterfaceIdAction(action=%r, interface_id=%r)" % (
            self.action,
            self.interface_id,
        )


@attr.s(auto_attribs=True, init=False, repr=False)
class PaymentSetKeyAction(PaymentUpdateAction):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.PaymentSetKeyActionSchema`."
    #: Optional :class:`str`
    key: typing.Optional[str]

    def __init__(
        self, *, action: typing.Optional[str] = None, key: typing.Optional[str] = None
    ) -> None:
        self.key = key
        super().__init__(action="setKey")

    def __repr__(self) -> str:
        return "PaymentSetKeyAction(action=%r, key=%r)" % (self.action, self.key)


@attr.s(auto_attribs=True, init=False, repr=False)
class PaymentSetMethodInfoInterfaceAction(PaymentUpdateAction):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.PaymentSetMethodInfoInterfaceActionSchema`."
    #: :class:`str`
    interface: typing.Optional[str]

    def __init__(
        self,
        *,
        action: typing.Optional[str] = None,
        interface: typing.Optional[str] = None
    ) -> None:
        self.interface = interface
        super().__init__(action="setMethodInfoInterface")

    def __repr__(self) -> str:
        return "PaymentSetMethodInfoInterfaceAction(action=%r, interface=%r)" % (
            self.action,
            self.interface,
        )


@attr.s(auto_attribs=True, init=False, repr=False)
class PaymentSetMethodInfoMethodAction(PaymentUpdateAction):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.PaymentSetMethodInfoMethodActionSchema`."
    #: Optional :class:`str`
    method: typing.Optional[str]

    def __init__(
        self,
        *,
        action: typing.Optional[str] = None,
        method: typing.Optional[str] = None
    ) -> None:
        self.method = method
        super().__init__(action="setMethodInfoMethod")

    def __repr__(self) -> str:
        return "PaymentSetMethodInfoMethodAction(action=%r, method=%r)" % (
            self.action,
            self.method,
        )


@attr.s(auto_attribs=True, init=False, repr=False)
class PaymentSetMethodInfoNameAction(PaymentUpdateAction):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.PaymentSetMethodInfoNameActionSchema`."
    #: Optional :class:`commercetools.types.LocalizedString`
    name: typing.Optional["LocalizedString"]

    def __init__(
        self,
        *,
        action: typing.Optional[str] = None,
        name: typing.Optional["LocalizedString"] = None
    ) -> None:
        self.name = name
        super().__init__(action="setMethodInfoName")

    def __repr__(self) -> str:
        return "PaymentSetMethodInfoNameAction(action=%r, name=%r)" % (
            self.action,
            self.name,
        )


@attr.s(auto_attribs=True, init=False, repr=False)
class PaymentSetStatusInterfaceCodeAction(PaymentUpdateAction):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.PaymentSetStatusInterfaceCodeActionSchema`."
    #: Optional :class:`str` `(Named` ``interfaceCode`` `in Commercetools)`
    interface_code: typing.Optional[str]

    def __init__(
        self,
        *,
        action: typing.Optional[str] = None,
        interface_code: typing.Optional[str] = None
    ) -> None:
        self.interface_code = interface_code
        super().__init__(action="setStatusInterfaceCode")

    def __repr__(self) -> str:
        return "PaymentSetStatusInterfaceCodeAction(action=%r, interface_code=%r)" % (
            self.action,
            self.interface_code,
        )


@attr.s(auto_attribs=True, init=False, repr=False)
class PaymentSetStatusInterfaceTextAction(PaymentUpdateAction):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.PaymentSetStatusInterfaceTextActionSchema`."
    #: :class:`str` `(Named` ``interfaceText`` `in Commercetools)`
    interface_text: typing.Optional[str]

    def __init__(
        self,
        *,
        action: typing.Optional[str] = None,
        interface_text: typing.Optional[str] = None
    ) -> None:
        self.interface_text = interface_text
        super().__init__(action="setStatusInterfaceText")

    def __repr__(self) -> str:
        return "PaymentSetStatusInterfaceTextAction(action=%r, interface_text=%r)" % (
            self.action,
            self.interface_text,
        )


@attr.s(auto_attribs=True, init=False, repr=False)
class PaymentTransitionStateAction(PaymentUpdateAction):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.PaymentTransitionStateActionSchema`."
    #: :class:`commercetools.types.StateReference`
    state: typing.Optional["StateReference"]
    #: Optional :class:`bool`
    force: typing.Optional[bool]

    def __init__(
        self,
        *,
        action: typing.Optional[str] = None,
        state: typing.Optional["StateReference"] = None,
        force: typing.Optional[bool] = None
    ) -> None:
        self.state = state
        self.force = force
        super().__init__(action="transitionState")

    def __repr__(self) -> str:
        return "PaymentTransitionStateAction(action=%r, state=%r, force=%r)" % (
            self.action,
            self.state,
            self.force,
        )
