"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from .basesdk import BaseSDK
from clerk import models
from clerk._hooks import HookContext
from clerk.types import BaseModel, Nullable, UNSET
import clerk.utils as utils
from typing import List, Optional, Union

class JwtTemplates(BaseSDK):
    
    
    def list(
        self, *,
        retries: Optional[Nullable[utils.RetryConfig]] = UNSET,
        server_url: Optional[str] = None,
        timeout_config: Optional[int] = None,
    ) -> List[models.JWTTemplate]:
        r"""List all templates

        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_config: Override the default request timeout configuration for this method in milliseconds
        """
        base_url = None
        url_variables = None
        if timeout_config is None:
            timeout_config = self.sdk_configuration.timeout_config
        
        if server_url is not None:
            base_url = server_url
        req = self.build_request(
            method="GET",
            path="/jwt_templates",
            base_url=base_url,
            url_variables=url_variables,
            request=None,
            request_body_required=False,
            request_has_path_params=False,
            request_has_query_params=True,
            user_agent_header="user-agent",
            accept_header_value="application/json",
            security=self.sdk_configuration.security,
            timeout_config=timeout_config,
        )
        
        if retries == UNSET:
            if self.sdk_configuration.retry_config is not UNSET:
                retries = self.sdk_configuration.retry_config

        retry_config = None
        if isinstance(retries, utils.RetryConfig):
            retry_config = (retries, [
                "429",
                "500",
                "502",
                "503",
                "504"
            ])                
        
        http_res = self.do_request(
            hook_ctx=HookContext(operation_id="ListJWTTemplates", oauth2_scopes=[], security_source=self.sdk_configuration.security),
            request=req,
            error_status_codes=["4XX","5XX"],
            retry_config=retry_config
        )
        
        
        if utils.match_response(http_res, "200", "application/json"):
            return utils.unmarshal_json(http_res.text, Optional[List[models.JWTTemplate]])
        if utils.match_response(http_res, ["4XX","5XX"], "*"):
            raise models.SDKError("API error occurred", http_res.status_code, http_res.text, http_res)
        
        content_type = http_res.headers.get("Content-Type")
        raise models.SDKError(f"Unexpected response received (code: {http_res.status_code}, type: {content_type})", http_res.status_code, http_res.text, http_res)
    
    
    async def list_async(
        self, *,
        retries: Optional[Nullable[utils.RetryConfig]] = UNSET,
        server_url: Optional[str] = None,
        timeout_config: Optional[int] = None,
    ) -> List[models.JWTTemplate]:
        r"""List all templates

        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_config: Override the default request timeout configuration for this method in milliseconds
        """
        base_url = None
        url_variables = None
        if timeout_config is None:
            timeout_config = self.sdk_configuration.timeout_config
        
        if server_url is not None:
            base_url = server_url
        req = self.build_request(
            method="GET",
            path="/jwt_templates",
            base_url=base_url,
            url_variables=url_variables,
            request=None,
            request_body_required=False,
            request_has_path_params=False,
            request_has_query_params=True,
            user_agent_header="user-agent",
            accept_header_value="application/json",
            security=self.sdk_configuration.security,
            timeout_config=timeout_config,
        )
        
        if retries == UNSET:
            if self.sdk_configuration.retry_config is not UNSET:
                retries = self.sdk_configuration.retry_config

        retry_config = None
        if isinstance(retries, utils.RetryConfig):
            retry_config = (retries, [
                "429",
                "500",
                "502",
                "503",
                "504"
            ])                
        
        http_res = await self.do_request_async(
            hook_ctx=HookContext(operation_id="ListJWTTemplates", oauth2_scopes=[], security_source=self.sdk_configuration.security),
            request=req,
            error_status_codes=["4XX","5XX"],
            retry_config=retry_config
        )
        
        
        if utils.match_response(http_res, "200", "application/json"):
            return utils.unmarshal_json(http_res.text, Optional[List[models.JWTTemplate]])
        if utils.match_response(http_res, ["4XX","5XX"], "*"):
            raise models.SDKError("API error occurred", http_res.status_code, http_res.text, http_res)
        
        content_type = http_res.headers.get("Content-Type")
        raise models.SDKError(f"Unexpected response received (code: {http_res.status_code}, type: {content_type})", http_res.status_code, http_res.text, http_res)
    
    
    def create(
        self, *,
        name: Optional[str] = None,
        claims: Optional[Union[models.CreateJWTTemplateClaims, models.CreateJWTTemplateClaimsTypedDict]] = None,
        lifetime: Optional[Nullable[float]] = None,
        allowed_clock_skew: Optional[Nullable[float]] = None,
        custom_signing_key: Optional[bool] = None,
        signing_algorithm: Optional[Nullable[str]] = None,
        signing_key: Optional[Nullable[str]] = None,
        retries: Optional[Nullable[utils.RetryConfig]] = UNSET,
        server_url: Optional[str] = None,
        timeout_config: Optional[int] = None,
    ) -> models.JWTTemplate:
        r"""Create a JWT template

        Create a new JWT template

        :param name: JWT template name
        :param claims: JWT template claims in JSON format
        :param lifetime: JWT token lifetime
        :param allowed_clock_skew: JWT token allowed clock skew
        :param custom_signing_key: Whether a custom signing key/algorithm is also provided for this template
        :param signing_algorithm: The custom signing algorithm to use when minting JWTs
        :param signing_key: The custom signing private key to use when minting JWTs
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_config: Override the default request timeout configuration for this method in milliseconds
        """
        base_url = None
        url_variables = None
        if timeout_config is None:
            timeout_config = self.sdk_configuration.timeout_config
        
        if server_url is not None:
            base_url = server_url
        
        request = models.CreateJWTTemplateRequestBody(
            name=name,
            claims=utils.unmarshal(claims, models.CreateJWTTemplateClaims) if not isinstance(claims, BaseModel) and claims is not None else claims,
            lifetime=lifetime,
            allowed_clock_skew=allowed_clock_skew,
            custom_signing_key=custom_signing_key,
            signing_algorithm=signing_algorithm,
            signing_key=signing_key,
        )
        
        req = self.build_request(
            method="POST",
            path="/jwt_templates",
            base_url=base_url,
            url_variables=url_variables,
            request=request,
            request_body_required=False,
            request_has_path_params=False,
            request_has_query_params=True,
            user_agent_header="user-agent",
            accept_header_value="application/json",
            security=self.sdk_configuration.security,
            get_serialized_body=lambda: utils.serialize_request_body(request, False, True, "json", Optional[models.CreateJWTTemplateRequestBody]),
            timeout_config=timeout_config,
        )
        
        if retries == UNSET:
            if self.sdk_configuration.retry_config is not UNSET:
                retries = self.sdk_configuration.retry_config

        retry_config = None
        if isinstance(retries, utils.RetryConfig):
            retry_config = (retries, [
                "429",
                "500",
                "502",
                "503",
                "504"
            ])                
        
        http_res = self.do_request(
            hook_ctx=HookContext(operation_id="CreateJWTTemplate", oauth2_scopes=[], security_source=self.sdk_configuration.security),
            request=req,
            error_status_codes=["400","402","422","4XX","5XX"],
            retry_config=retry_config
        )
        
        
        if utils.match_response(http_res, "200", "application/json"):
            return utils.unmarshal_json(http_res.text, Optional[models.JWTTemplate])
        if utils.match_response(http_res, ["400","402","422"], "application/json"):
            data = utils.unmarshal_json(http_res.text, models.ClerkErrorsData)
            raise models.ClerkErrors(data=data)
        if utils.match_response(http_res, ["4XX","5XX"], "*"):
            raise models.SDKError("API error occurred", http_res.status_code, http_res.text, http_res)
        
        content_type = http_res.headers.get("Content-Type")
        raise models.SDKError(f"Unexpected response received (code: {http_res.status_code}, type: {content_type})", http_res.status_code, http_res.text, http_res)
    
    
    async def create_async(
        self, *,
        name: Optional[str] = None,
        claims: Optional[Union[models.CreateJWTTemplateClaims, models.CreateJWTTemplateClaimsTypedDict]] = None,
        lifetime: Optional[Nullable[float]] = None,
        allowed_clock_skew: Optional[Nullable[float]] = None,
        custom_signing_key: Optional[bool] = None,
        signing_algorithm: Optional[Nullable[str]] = None,
        signing_key: Optional[Nullable[str]] = None,
        retries: Optional[Nullable[utils.RetryConfig]] = UNSET,
        server_url: Optional[str] = None,
        timeout_config: Optional[int] = None,
    ) -> models.JWTTemplate:
        r"""Create a JWT template

        Create a new JWT template

        :param name: JWT template name
        :param claims: JWT template claims in JSON format
        :param lifetime: JWT token lifetime
        :param allowed_clock_skew: JWT token allowed clock skew
        :param custom_signing_key: Whether a custom signing key/algorithm is also provided for this template
        :param signing_algorithm: The custom signing algorithm to use when minting JWTs
        :param signing_key: The custom signing private key to use when minting JWTs
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_config: Override the default request timeout configuration for this method in milliseconds
        """
        base_url = None
        url_variables = None
        if timeout_config is None:
            timeout_config = self.sdk_configuration.timeout_config
        
        if server_url is not None:
            base_url = server_url
        
        request = models.CreateJWTTemplateRequestBody(
            name=name,
            claims=utils.unmarshal(claims, models.CreateJWTTemplateClaims) if not isinstance(claims, BaseModel) and claims is not None else claims,
            lifetime=lifetime,
            allowed_clock_skew=allowed_clock_skew,
            custom_signing_key=custom_signing_key,
            signing_algorithm=signing_algorithm,
            signing_key=signing_key,
        )
        
        req = self.build_request(
            method="POST",
            path="/jwt_templates",
            base_url=base_url,
            url_variables=url_variables,
            request=request,
            request_body_required=False,
            request_has_path_params=False,
            request_has_query_params=True,
            user_agent_header="user-agent",
            accept_header_value="application/json",
            security=self.sdk_configuration.security,
            get_serialized_body=lambda: utils.serialize_request_body(request, False, True, "json", Optional[models.CreateJWTTemplateRequestBody]),
            timeout_config=timeout_config,
        )
        
        if retries == UNSET:
            if self.sdk_configuration.retry_config is not UNSET:
                retries = self.sdk_configuration.retry_config

        retry_config = None
        if isinstance(retries, utils.RetryConfig):
            retry_config = (retries, [
                "429",
                "500",
                "502",
                "503",
                "504"
            ])                
        
        http_res = await self.do_request_async(
            hook_ctx=HookContext(operation_id="CreateJWTTemplate", oauth2_scopes=[], security_source=self.sdk_configuration.security),
            request=req,
            error_status_codes=["400","402","422","4XX","5XX"],
            retry_config=retry_config
        )
        
        
        if utils.match_response(http_res, "200", "application/json"):
            return utils.unmarshal_json(http_res.text, Optional[models.JWTTemplate])
        if utils.match_response(http_res, ["400","402","422"], "application/json"):
            data = utils.unmarshal_json(http_res.text, models.ClerkErrorsData)
            raise models.ClerkErrors(data=data)
        if utils.match_response(http_res, ["4XX","5XX"], "*"):
            raise models.SDKError("API error occurred", http_res.status_code, http_res.text, http_res)
        
        content_type = http_res.headers.get("Content-Type")
        raise models.SDKError(f"Unexpected response received (code: {http_res.status_code}, type: {content_type})", http_res.status_code, http_res.text, http_res)
    
    
    def get(
        self, *,
        template_id: str,
        retries: Optional[Nullable[utils.RetryConfig]] = UNSET,
        server_url: Optional[str] = None,
        timeout_config: Optional[int] = None,
    ) -> models.JWTTemplate:
        r"""Retrieve a template

        Retrieve the details of a given JWT template

        :param template_id: JWT Template ID
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_config: Override the default request timeout configuration for this method in milliseconds
        """
        base_url = None
        url_variables = None
        if timeout_config is None:
            timeout_config = self.sdk_configuration.timeout_config
        
        if server_url is not None:
            base_url = server_url
        
        request = models.GetJWTTemplateRequest(
            template_id=template_id,
        )
        
        req = self.build_request(
            method="GET",
            path="/jwt_templates/{template_id}",
            base_url=base_url,
            url_variables=url_variables,
            request=request,
            request_body_required=False,
            request_has_path_params=True,
            request_has_query_params=True,
            user_agent_header="user-agent",
            accept_header_value="application/json",
            security=self.sdk_configuration.security,
            timeout_config=timeout_config,
        )
        
        if retries == UNSET:
            if self.sdk_configuration.retry_config is not UNSET:
                retries = self.sdk_configuration.retry_config

        retry_config = None
        if isinstance(retries, utils.RetryConfig):
            retry_config = (retries, [
                "429",
                "500",
                "502",
                "503",
                "504"
            ])                
        
        http_res = self.do_request(
            hook_ctx=HookContext(operation_id="GetJWTTemplate", oauth2_scopes=[], security_source=self.sdk_configuration.security),
            request=req,
            error_status_codes=["404","4XX","5XX"],
            retry_config=retry_config
        )
        
        
        if utils.match_response(http_res, "200", "application/json"):
            return utils.unmarshal_json(http_res.text, Optional[models.JWTTemplate])
        if utils.match_response(http_res, "404", "application/json"):
            data = utils.unmarshal_json(http_res.text, models.ClerkErrorsData)
            raise models.ClerkErrors(data=data)
        if utils.match_response(http_res, ["4XX","5XX"], "*"):
            raise models.SDKError("API error occurred", http_res.status_code, http_res.text, http_res)
        
        content_type = http_res.headers.get("Content-Type")
        raise models.SDKError(f"Unexpected response received (code: {http_res.status_code}, type: {content_type})", http_res.status_code, http_res.text, http_res)
    
    
    async def get_async(
        self, *,
        template_id: str,
        retries: Optional[Nullable[utils.RetryConfig]] = UNSET,
        server_url: Optional[str] = None,
        timeout_config: Optional[int] = None,
    ) -> models.JWTTemplate:
        r"""Retrieve a template

        Retrieve the details of a given JWT template

        :param template_id: JWT Template ID
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_config: Override the default request timeout configuration for this method in milliseconds
        """
        base_url = None
        url_variables = None
        if timeout_config is None:
            timeout_config = self.sdk_configuration.timeout_config
        
        if server_url is not None:
            base_url = server_url
        
        request = models.GetJWTTemplateRequest(
            template_id=template_id,
        )
        
        req = self.build_request(
            method="GET",
            path="/jwt_templates/{template_id}",
            base_url=base_url,
            url_variables=url_variables,
            request=request,
            request_body_required=False,
            request_has_path_params=True,
            request_has_query_params=True,
            user_agent_header="user-agent",
            accept_header_value="application/json",
            security=self.sdk_configuration.security,
            timeout_config=timeout_config,
        )
        
        if retries == UNSET:
            if self.sdk_configuration.retry_config is not UNSET:
                retries = self.sdk_configuration.retry_config

        retry_config = None
        if isinstance(retries, utils.RetryConfig):
            retry_config = (retries, [
                "429",
                "500",
                "502",
                "503",
                "504"
            ])                
        
        http_res = await self.do_request_async(
            hook_ctx=HookContext(operation_id="GetJWTTemplate", oauth2_scopes=[], security_source=self.sdk_configuration.security),
            request=req,
            error_status_codes=["404","4XX","5XX"],
            retry_config=retry_config
        )
        
        
        if utils.match_response(http_res, "200", "application/json"):
            return utils.unmarshal_json(http_res.text, Optional[models.JWTTemplate])
        if utils.match_response(http_res, "404", "application/json"):
            data = utils.unmarshal_json(http_res.text, models.ClerkErrorsData)
            raise models.ClerkErrors(data=data)
        if utils.match_response(http_res, ["4XX","5XX"], "*"):
            raise models.SDKError("API error occurred", http_res.status_code, http_res.text, http_res)
        
        content_type = http_res.headers.get("Content-Type")
        raise models.SDKError(f"Unexpected response received (code: {http_res.status_code}, type: {content_type})", http_res.status_code, http_res.text, http_res)
    
    
    def update(
        self, *,
        template_id: str,
        name: Optional[str] = None,
        claims: Optional[Union[models.UpdateJWTTemplateClaims, models.UpdateJWTTemplateClaimsTypedDict]] = None,
        lifetime: Optional[Nullable[float]] = None,
        allowed_clock_skew: Optional[Nullable[float]] = None,
        custom_signing_key: Optional[bool] = None,
        signing_algorithm: Optional[Nullable[str]] = None,
        signing_key: Optional[Nullable[str]] = None,
        retries: Optional[Nullable[utils.RetryConfig]] = UNSET,
        server_url: Optional[str] = None,
        timeout_config: Optional[int] = None,
    ) -> models.JWTTemplate:
        r"""Update a JWT template

        Updates an existing JWT template

        :param template_id: The ID of the JWT template to update
        :param name: JWT template name
        :param claims: JWT template claims in JSON format
        :param lifetime: JWT token lifetime
        :param allowed_clock_skew: JWT token allowed clock skew
        :param custom_signing_key: Whether a custom signing key/algorithm is also provided for this template
        :param signing_algorithm: The custom signing algorithm to use when minting JWTs
        :param signing_key: The custom signing private key to use when minting JWTs
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_config: Override the default request timeout configuration for this method in milliseconds
        """
        base_url = None
        url_variables = None
        if timeout_config is None:
            timeout_config = self.sdk_configuration.timeout_config
        
        if server_url is not None:
            base_url = server_url
        
        request = models.UpdateJWTTemplateRequest(
            template_id=template_id,
            request_body=models.UpdateJWTTemplateRequestBody(
                name=name,
                claims=utils.unmarshal(claims, models.UpdateJWTTemplateClaims) if not isinstance(claims, BaseModel) and claims is not None else claims,
                lifetime=lifetime,
                allowed_clock_skew=allowed_clock_skew,
                custom_signing_key=custom_signing_key,
                signing_algorithm=signing_algorithm,
                signing_key=signing_key,
            ),
        )
        
        req = self.build_request(
            method="PATCH",
            path="/jwt_templates/{template_id}",
            base_url=base_url,
            url_variables=url_variables,
            request=request,
            request_body_required=False,
            request_has_path_params=True,
            request_has_query_params=True,
            user_agent_header="user-agent",
            accept_header_value="application/json",
            security=self.sdk_configuration.security,
            get_serialized_body=lambda: utils.serialize_request_body(request.request_body, False, True, "json", Optional[models.UpdateJWTTemplateRequestBody]),
            timeout_config=timeout_config,
        )
        
        if retries == UNSET:
            if self.sdk_configuration.retry_config is not UNSET:
                retries = self.sdk_configuration.retry_config

        retry_config = None
        if isinstance(retries, utils.RetryConfig):
            retry_config = (retries, [
                "429",
                "500",
                "502",
                "503",
                "504"
            ])                
        
        http_res = self.do_request(
            hook_ctx=HookContext(operation_id="UpdateJWTTemplate", oauth2_scopes=[], security_source=self.sdk_configuration.security),
            request=req,
            error_status_codes=["400","402","422","4XX","5XX"],
            retry_config=retry_config
        )
        
        
        if utils.match_response(http_res, "200", "application/json"):
            return utils.unmarshal_json(http_res.text, Optional[models.JWTTemplate])
        if utils.match_response(http_res, ["400","402","422"], "application/json"):
            data = utils.unmarshal_json(http_res.text, models.ClerkErrorsData)
            raise models.ClerkErrors(data=data)
        if utils.match_response(http_res, ["4XX","5XX"], "*"):
            raise models.SDKError("API error occurred", http_res.status_code, http_res.text, http_res)
        
        content_type = http_res.headers.get("Content-Type")
        raise models.SDKError(f"Unexpected response received (code: {http_res.status_code}, type: {content_type})", http_res.status_code, http_res.text, http_res)
    
    
    async def update_async(
        self, *,
        template_id: str,
        name: Optional[str] = None,
        claims: Optional[Union[models.UpdateJWTTemplateClaims, models.UpdateJWTTemplateClaimsTypedDict]] = None,
        lifetime: Optional[Nullable[float]] = None,
        allowed_clock_skew: Optional[Nullable[float]] = None,
        custom_signing_key: Optional[bool] = None,
        signing_algorithm: Optional[Nullable[str]] = None,
        signing_key: Optional[Nullable[str]] = None,
        retries: Optional[Nullable[utils.RetryConfig]] = UNSET,
        server_url: Optional[str] = None,
        timeout_config: Optional[int] = None,
    ) -> models.JWTTemplate:
        r"""Update a JWT template

        Updates an existing JWT template

        :param template_id: The ID of the JWT template to update
        :param name: JWT template name
        :param claims: JWT template claims in JSON format
        :param lifetime: JWT token lifetime
        :param allowed_clock_skew: JWT token allowed clock skew
        :param custom_signing_key: Whether a custom signing key/algorithm is also provided for this template
        :param signing_algorithm: The custom signing algorithm to use when minting JWTs
        :param signing_key: The custom signing private key to use when minting JWTs
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_config: Override the default request timeout configuration for this method in milliseconds
        """
        base_url = None
        url_variables = None
        if timeout_config is None:
            timeout_config = self.sdk_configuration.timeout_config
        
        if server_url is not None:
            base_url = server_url
        
        request = models.UpdateJWTTemplateRequest(
            template_id=template_id,
            request_body=models.UpdateJWTTemplateRequestBody(
                name=name,
                claims=utils.unmarshal(claims, models.UpdateJWTTemplateClaims) if not isinstance(claims, BaseModel) and claims is not None else claims,
                lifetime=lifetime,
                allowed_clock_skew=allowed_clock_skew,
                custom_signing_key=custom_signing_key,
                signing_algorithm=signing_algorithm,
                signing_key=signing_key,
            ),
        )
        
        req = self.build_request(
            method="PATCH",
            path="/jwt_templates/{template_id}",
            base_url=base_url,
            url_variables=url_variables,
            request=request,
            request_body_required=False,
            request_has_path_params=True,
            request_has_query_params=True,
            user_agent_header="user-agent",
            accept_header_value="application/json",
            security=self.sdk_configuration.security,
            get_serialized_body=lambda: utils.serialize_request_body(request.request_body, False, True, "json", Optional[models.UpdateJWTTemplateRequestBody]),
            timeout_config=timeout_config,
        )
        
        if retries == UNSET:
            if self.sdk_configuration.retry_config is not UNSET:
                retries = self.sdk_configuration.retry_config

        retry_config = None
        if isinstance(retries, utils.RetryConfig):
            retry_config = (retries, [
                "429",
                "500",
                "502",
                "503",
                "504"
            ])                
        
        http_res = await self.do_request_async(
            hook_ctx=HookContext(operation_id="UpdateJWTTemplate", oauth2_scopes=[], security_source=self.sdk_configuration.security),
            request=req,
            error_status_codes=["400","402","422","4XX","5XX"],
            retry_config=retry_config
        )
        
        
        if utils.match_response(http_res, "200", "application/json"):
            return utils.unmarshal_json(http_res.text, Optional[models.JWTTemplate])
        if utils.match_response(http_res, ["400","402","422"], "application/json"):
            data = utils.unmarshal_json(http_res.text, models.ClerkErrorsData)
            raise models.ClerkErrors(data=data)
        if utils.match_response(http_res, ["4XX","5XX"], "*"):
            raise models.SDKError("API error occurred", http_res.status_code, http_res.text, http_res)
        
        content_type = http_res.headers.get("Content-Type")
        raise models.SDKError(f"Unexpected response received (code: {http_res.status_code}, type: {content_type})", http_res.status_code, http_res.text, http_res)
    
    
    def delete(
        self, *,
        template_id: str,
        retries: Optional[Nullable[utils.RetryConfig]] = UNSET,
        server_url: Optional[str] = None,
        timeout_config: Optional[int] = None,
    ) -> models.DeletedObject:
        r"""Delete a Template

        :param template_id: JWT Template ID
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_config: Override the default request timeout configuration for this method in milliseconds
        """
        base_url = None
        url_variables = None
        if timeout_config is None:
            timeout_config = self.sdk_configuration.timeout_config
        
        if server_url is not None:
            base_url = server_url
        
        request = models.DeleteJWTTemplateRequest(
            template_id=template_id,
        )
        
        req = self.build_request(
            method="DELETE",
            path="/jwt_templates/{template_id}",
            base_url=base_url,
            url_variables=url_variables,
            request=request,
            request_body_required=False,
            request_has_path_params=True,
            request_has_query_params=True,
            user_agent_header="user-agent",
            accept_header_value="application/json",
            security=self.sdk_configuration.security,
            timeout_config=timeout_config,
        )
        
        if retries == UNSET:
            if self.sdk_configuration.retry_config is not UNSET:
                retries = self.sdk_configuration.retry_config

        retry_config = None
        if isinstance(retries, utils.RetryConfig):
            retry_config = (retries, [
                "429",
                "500",
                "502",
                "503",
                "504"
            ])                
        
        http_res = self.do_request(
            hook_ctx=HookContext(operation_id="DeleteJWTTemplate", oauth2_scopes=[], security_source=self.sdk_configuration.security),
            request=req,
            error_status_codes=["403","404","4XX","5XX"],
            retry_config=retry_config
        )
        
        
        if utils.match_response(http_res, "200", "application/json"):
            return utils.unmarshal_json(http_res.text, Optional[models.DeletedObject])
        if utils.match_response(http_res, ["403","404"], "application/json"):
            data = utils.unmarshal_json(http_res.text, models.ClerkErrorsData)
            raise models.ClerkErrors(data=data)
        if utils.match_response(http_res, ["4XX","5XX"], "*"):
            raise models.SDKError("API error occurred", http_res.status_code, http_res.text, http_res)
        
        content_type = http_res.headers.get("Content-Type")
        raise models.SDKError(f"Unexpected response received (code: {http_res.status_code}, type: {content_type})", http_res.status_code, http_res.text, http_res)
    
    
    async def delete_async(
        self, *,
        template_id: str,
        retries: Optional[Nullable[utils.RetryConfig]] = UNSET,
        server_url: Optional[str] = None,
        timeout_config: Optional[int] = None,
    ) -> models.DeletedObject:
        r"""Delete a Template

        :param template_id: JWT Template ID
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_config: Override the default request timeout configuration for this method in milliseconds
        """
        base_url = None
        url_variables = None
        if timeout_config is None:
            timeout_config = self.sdk_configuration.timeout_config
        
        if server_url is not None:
            base_url = server_url
        
        request = models.DeleteJWTTemplateRequest(
            template_id=template_id,
        )
        
        req = self.build_request(
            method="DELETE",
            path="/jwt_templates/{template_id}",
            base_url=base_url,
            url_variables=url_variables,
            request=request,
            request_body_required=False,
            request_has_path_params=True,
            request_has_query_params=True,
            user_agent_header="user-agent",
            accept_header_value="application/json",
            security=self.sdk_configuration.security,
            timeout_config=timeout_config,
        )
        
        if retries == UNSET:
            if self.sdk_configuration.retry_config is not UNSET:
                retries = self.sdk_configuration.retry_config

        retry_config = None
        if isinstance(retries, utils.RetryConfig):
            retry_config = (retries, [
                "429",
                "500",
                "502",
                "503",
                "504"
            ])                
        
        http_res = await self.do_request_async(
            hook_ctx=HookContext(operation_id="DeleteJWTTemplate", oauth2_scopes=[], security_source=self.sdk_configuration.security),
            request=req,
            error_status_codes=["403","404","4XX","5XX"],
            retry_config=retry_config
        )
        
        
        if utils.match_response(http_res, "200", "application/json"):
            return utils.unmarshal_json(http_res.text, Optional[models.DeletedObject])
        if utils.match_response(http_res, ["403","404"], "application/json"):
            data = utils.unmarshal_json(http_res.text, models.ClerkErrorsData)
            raise models.ClerkErrors(data=data)
        if utils.match_response(http_res, ["4XX","5XX"], "*"):
            raise models.SDKError("API error occurred", http_res.status_code, http_res.text, http_res)
        
        content_type = http_res.headers.get("Content-Type")
        raise models.SDKError(f"Unexpected response received (code: {http_res.status_code}, type: {content_type})", http_res.status_code, http_res.text, http_res)
    
