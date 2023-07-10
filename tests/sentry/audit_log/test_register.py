from sentry import audit_log
from sentry.testutils import TestCase
from sentry.testutils.silo import region_silo_test


@region_silo_test
class AuditLogEventRegisterTest(TestCase):
    def test_get_api_names(self):
        audit_log_api_name_list = [
            "member.invite",
            "member.add",
            "member.accept-invite",
            "member.edit",
            "member.remove",
            "member.join-team",
            "member.leave-team",
            "member.pending",
            "org.create",
            "org.edit",
            "org.remove",
            "org.restore",
            "team.create",
            "team.edit",
            "team.remove",
            "project.create",
            "project.edit",
            "project.change-performance-issue-detection",
            "project.remove",
            "project.remove-with-origin",
            "project.request-transfer",
            "project.accept-transfer",
            "project.enable",
            "project.disable",
            "tagkey.remove",
            "projectkey.create",
            "projectkey.edit",
            "projectkey.remove",
            "projectkey.change",
            "sso.enable",
            "sso.disable",
            "sso.edit",
            "sso-identity.link",
            "api-key.create",
            "api-key.edit",
            "api-key.remove",
            "rule.create",
            "rule.edit",
            "rule.remove",
            "rule.mute",
            "servicehook.create",
            "servicehook.edit",
            "servicehook.remove",
            "integration.upgrade",
            "integration.add",
            "integration.edit",
            "integration.remove",
            "sentry-app.add",
            "sentry-app.remove",
            "sentry-app.install",
            "sentry-app.uninstall",
            "sampling_priority.enabled",
            "sampling_priority.disabled",
            "monitor.add",
            "monitor.edit",
            "monitor.environment.remove",
            "monitor.remove",
            "internal-integration.create",
            "internal-integration.add-token",
            "internal-integration.remove-token",
            "invite-request.create",
            "invite-request.remove",
            "alertrule.create",
            "alertrule.edit",
            "alertrule.remove",
            "alertrule.mute",
            "notification_action.create",
            "notification_action.edit",
            "notification_action.remove",
            "team-and-project.created",
            "org-auth-token.create",
            "org-auth-token.remove",
        ]

        assert set(audit_log.get_api_names()) == set(audit_log_api_name_list)
