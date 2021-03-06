odoo.define('account_analytic_plans.custom', function (require) {
"use strict";

var widgets = require('account.reconciliation');
var core = require('web.core');

var _t = core._t;

widgets.bankStatementReconciliation.include({
    init: function(parent, context) {
        var FieldMany2One = core.form_widget_registry.get('many2one');
        this._super(parent, context);
        delete this.create_form_fields.analytic_account_id;
        this.create_form_fields["analytic_plan"] = {
            id: "analytic_plan",
            index: 4,
            corresponding_property: "analytics_id",
            label: _t("Analytic Distribution"),
            required: false,
            group: "analytic.group_analytic_accounting",
            constructor: FieldMany2One,
            field_properties: {
                relation: "account.analytic.plan.instance",
                string: _t("Analytic Distribution"),
                type: "many2one",
            }
        };
    },
});

widgets.bankStatementReconciliationLine.include({
    prepareCreatedMoveLineForPersisting: function(line) {
        var dict = this._super(line);
        if (line.analytics_id) dict['analytics_id'] = line.analytics_id;
        if (dict["analytic_account_id"] !== undefined) delete dict["analytic_account_id"];
        return dict;
    },
});

});