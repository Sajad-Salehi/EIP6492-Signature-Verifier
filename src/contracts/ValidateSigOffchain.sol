pragma solidity ^0.8.21;
// SPDX-License-Identifier: MIT

import { UniversalSigValidator } from "./UniversalSigValidator.sol";

// this is a helper so we can perform validation in a single eth_call without pre-deploying a singleton
contract ValidateSigOffchain {
  constructor (address _signer, bytes32 _hash, bytes memory _signature) {
    UniversalSigValidator validator = new UniversalSigValidator();
    bool isValidSig = validator.isValidSigWithSideEffects(_signer, _hash, _signature);
    assembly {
      mstore(0, isValidSig)
      return(31, 1)
    }
  }
}